import click
import clipboard
from password_generator import PasswordGenerator

# python decorators
@click.command()
@click.option('-l', '--length', default=8, help='Length of password')
@click.option('-n/-nn', '--numbers/--no-numbers',default=True, help ='Add or remove numbers from your password')
@click.option('-sm/-nsm', '--symbol/--no-symbol',default=True, help ='Add or remove symbol from your password')
@click.option('-s/-ns', '--save/--no-save',default=False, help ='Save password to text file')

def main(length, numbers, symbol, save):
    passgen = PasswordGenerator(length, numbers, symbol, save)
    password = passgen.create_password()

    clipboard.copy(password)

    click.echo(f'{click.style("password", fg="blue")}:{password}')
    click.secho("Password copied to clipboard", fg='green')

    if save:
        click.secho('Password saved to txt', fg ='blue')
        passgen.save_password(password)

if __name__ == '__main__':
    main()