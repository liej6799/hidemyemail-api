
import sys
import click
from pyicloud import PyiCloudService


@click.command()
@click.option('--username', prompt=True)
@click.option('--password', prompt=True, hide_input=True,)
def login(username, password):
    api = PyiCloudService(username,password)
    if api.requires_2fa:
        click.echo("Two-factor authentication required.")
        code = click.prompt("Enter the code you received of one of your approved devices: ")
        result = api.validate_2fa_code(code)
        click.echo("Code validation result: %s" % result)

        if not result:
            click.echo("Failed to verify security code")
            sys.exit(1)

        if not api.is_trusted_session:
            click.echo("Session is not trusted. Requesting trust...")
            result = api.trust_session()
            click.echo("Session trust result %s" % result)

            if not result:
                click.echo("Failed to request trust. You will likely be prompted for the code again in the coming weeks")
    elif api.requires_2sa:
        click.echo("Two-step authentication required. Your trusted devices are:")

        devices = api.trusted_devices
        for i, device in enumerate(devices):
            click.echo(
                "  %s: %s" % (i, device.get('deviceName',
                "SMS to %s" % device.get('phoneNumber')))
            )

        device = click.prompt('Which device would you like to use?', default=0)
        device = devices[device]
        if not api.send_verification_code(device):
            click.echo("Failed to send verification code")
            sys.exit(1)

        code = click.prompt('Please enter validation code')
        if not api.validate_verification_code(device, code):
            click.echo("Failed to verify verification code")
            sys.exit(1)


if __name__ == '__main__':
    login()
