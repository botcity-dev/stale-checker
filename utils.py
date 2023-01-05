from botcity.plugins.slack import BotSlackPlugin, Message, Color, Author, Field

import os
import pathlib
import subprocess

PIPE = subprocess.PIPE

client = BotSlackPlugin(
    slack_token=os.getenv("SLACK_TOKEN"),
    channel=os.getenv("CHANNEL")
)


def checkout_repo(folder: pathlib.Path, repo: str) -> None:
    cmd = f"git clone --depth 1 {repo} ."
    cmd = os.path.expandvars(cmd)
    proc = subprocess.Popen(cmd.split(" "), cwd=folder)
    proc.wait()


def fetch_repo(folder: pathlib.Path) -> None:
    cmd = f"git fetch --tags"
    proc = subprocess.Popen(cmd.split(" "), cwd=folder)
    proc.wait()


def get_last_date_commit(folder: pathlib.Path) -> str:
    command = "git log -1 --format=%ct"
    process = subprocess.Popen(command.split(" "), cwd=folder, stdout=PIPE, stderr=PIPE)
    stdoutput, _ = process.communicate()

    return stdoutput.decode("utf-8").strip()


def get_last_date_tag(folder: pathlib.Path) -> str:
    command = "git log --tags -1 --format=%ct"
    process = subprocess.Popen(command.split(" "), cwd=folder, stdout=PIPE, stderr=PIPE)
    stdoutput, _ = process.communicate()

    return stdoutput.decode("utf-8").strip()


def send_message(project_name: str, difference_of_days: str, owner: str):
    message = Message(
        title="Time for new release?",
        color=Color.YELLOW
    )
    message.author = Author(
        author_name="Stale Repository Checker",
        author_icon="https://documentation.botcity.dev/assets/logo.png",
    )
    url_repository = f"https://github.com/{owner}/{project_name}"
    message.fields = [
        Field(title="Project name", value=project_name, short=False),
        Field(title="Link to repository", value=url_repository),
        Field(title="Difference of days", value=difference_of_days, short=False)
    ]

    client.send_message(message=message)
