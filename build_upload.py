import os
import subprocess
import sys

clean_cmd_win = "if exist dist rmdir /s /q dist"
clean_cmd_linux = "rm -rf dist"

build_cmd = "python -m build"
upload_cmd = "python -m twine upload dist/*"


def build_and_upload():
    try:
        # 1. 清理旧的构建文件
        if sys.platform == "win32":
            clean_cmd = clean_cmd_win
        else:
            clean_cmd = clean_cmd_linux

        subprocess.run(clean_cmd, shell=True, check=True)

        # 2. 构建包
        print("开始构建...")
        subprocess.run(build_cmd, check=True)

        # 3. 上传到 PyPI
        print("开始上传...")
        subprocess.run(upload_cmd, check=True)

        print("构建和上传成功！")

    except subprocess.CalledProcessError as e:
        print(f"错误: 命令执行失败: {e}")
        sys.exit(1)


if __name__ == "__main__":
    build_and_upload()
