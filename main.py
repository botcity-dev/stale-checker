import argparse
import utils
import tempfile
import shutil
from datetime import datetime

parser = argparse.ArgumentParser(prog='Verify commits and tags in github')
parser.add_argument("-days", action="store", default=15)
args = parser.parse_args()

days = int(args.days)

with open('repos.txt') as f:
    lines = [line.rstrip() for line in f]


print(f"Execution  in {len(lines)} repositories")

for line in lines:
    tmp_folder = tempfile.mkdtemp()
    project_name = line.split("/")[4].replace(".git", "")
    print(f"Execution in {project_name}")
    try:
        utils.checkout_repo(folder=tmp_folder, repo=line)
        utils.fetch_repo(folder=tmp_folder)

        last_date_commit = utils.get_last_date_commit(folder=tmp_folder)

        last_date_tag = utils.get_last_date_tag(folder=tmp_folder)

        if not last_date_tag:
            print(f"\033[33m Project {project_name} has no tags")
            continue

        timestamp_tag = float(last_date_tag)
        timestamp_commit = float(last_date_commit)

        date_latest_commit = datetime.fromtimestamp(timestamp_commit)
        date_latest_tag = datetime.fromtimestamp(timestamp_tag)

        difference_of_days = (datetime.now() - date_latest_commit).days

        if date_latest_commit > date_latest_tag and difference_of_days > days:
            utils.send_message(project_name=project_name, difference_of_days=str(difference_of_days))
    finally:
        shutil.rmtree(tmp_folder)
