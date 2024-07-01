from time import sleep
from celery import shared_task
import subprocess

@shared_task
def notify_customers(message):
    print('sending 10k emailes....')
    print(message)
    sleep(10)
    print('Emails were successfully sent!')

@shared_task
def run_scrap_channels(keywords):
    for keyword in keywords:
        try:
            execute_command(keyword)
        except Exception as e:
            print(f"An error occurred while processing keyword '{keyword}': {str(e)}")

def execute_command(keyword):
    command = [
        'docker', 'run', '-t', 'heekim1/mediascrap:latest',
        'python', '/app/scrap_channels.py',
        '--keyword', keyword,
        '--start_year', '2012',
        '--end_year', '2024',
        '--s3_upload',
        '--output_dir', 'out'
    ]
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        raise Exception(f"Command execution failed with return code {e.returncode}: {e.output.decode()}")