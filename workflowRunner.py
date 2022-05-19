import os
import pwd
import argparse

from auto_generated_pipieline_framework.config import demo
from auto_generated_pipieline_framework.workflows import databathing_workflow
from auto_generated_pipieline_framework.utils import spark_util
from auto_generated_pipieline_framework.config import df_storage


def manage_workflow():
    """run the pipeline
    """
    databathing_workflow.run()


def main():
    parser = argparse.ArgumentParser(description="uploader")

    parser.add_argument("--extracts_yaml",
                        "-e",
                        help="extract yaml",
                        required=True)

    parser.add_argument("--transforms_yaml",
                        "-t",
                        help="transform yaml",
                        required=True)

    parser.add_argument("--loaders_yaml",
                        "-l",
                        help="loader yaml",
                        required=True)

    args = parser.parse_args()

    user = pwd.getpwuid(os.getuid())[0]
    spark_util.init_spark(demo.project_name, user)


    df_storage.yaml_storage["extracts"] = args.extracts_yaml
    df_storage.yaml_storage["transforms"] = args.transforms_yaml
    df_storage.yaml_storage["loaders"] = args.loaders_yaml

    manage_workflow()


if __name__ == "__main__":
    main()
