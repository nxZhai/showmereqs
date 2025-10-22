
import re
from collections import OrderedDict

from tomlkit import array, dumps, parse, table

REQ_NAME_RE = re.compile(r"^[A-Za-z0-9_.\-]+")


def norm_name(dep_str: str) -> str:
    """从 'torch==2.5.1' 提取包名并统一小写，用于对比/去重。"""
    dep_str = dep_str.strip().strip('"').strip("'")
    m = REQ_NAME_RE.match(dep_str)
    return m.group(0).lower() if m else dep_str.lower()


def parse_requirement_line(line: str):
    """去掉注释并返回依赖字符串，如 'torch==2.5.1'；无效行返回 None。"""
    line = line.strip()
    if not line or line.startswith("#"):
        return None
    if "#" in line:
        line = line.split("#", 1)[0].strip()
    return line or None


def update_dependencies_in_section(section, new_deps_list):
    """
    将 new_deps_list 融合进 section['dependencies']：
    - 同名包覆盖旧条目
    - 新包追加
    - 已有且相同保持不变
    并格式化为多行数组
    """
    # 读取已有依赖（若无则空列表）
    existing = list(section.get("dependencies", []))

    # 以“首次出现顺序 + 后续新增”来组织，避免排序打乱你的原始顺序
    ordered = OrderedDict()
    for dep in existing:
        ordered[norm_name(dep)] = str(dep)

    for dep in new_deps_list:
        ordered[norm_name(dep)] = dep  # 覆盖或新增

    # 生成 tomlkit 的多行数组
    arr = array()
    for dep in ordered.values():
        arr.append(dep)
    arr.multiline(True)  # 多行显示
    section["dependencies"] = arr


def main(req_path: str, toml_path: str, out_path: str | None = None):
    # 读取并解析 TOML 文本（tomlkit 可保留注释/格式）
    with open(toml_path, "r", encoding="utf-8") as f:
        doc = parse(f.read())

    # 目标段落优先级：PEP 621 -> Poetry
    target = None
    if "project" in doc:
        target = doc["project"]
    elif "tool" in doc and "poetry" in doc["tool"]:
        target = doc["tool"]["poetry"]
    else:
        # 没有就创建 PEP 621 的 [project]
        doc["project"] = table()
        target = doc["project"]

    # 从 requirements 读取新依赖
    new_deps = []
    with open(req_path, "r", encoding="utf-8") as f:
        for line in f:
            dep = parse_requirement_line(line)
            if dep:
                new_deps.append(dep)

    # 更新目标段落的 dependencies
    update_dependencies_in_section(target, new_deps)

    # 如果顶层误放了 dependencies，把它删掉，避免重复/冲突
    if "dependencies" in doc:
        del doc["dependencies"]

    # 写回
    out_path = out_path or toml_path
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(dumps(doc))

    print(f"✅ 已更新并格式化 {out_path}")


if __name__ == "__main__":
    # 用法示例
    # main("requirements.txt", "pyproject.toml")
    import sys

    if len(sys.argv) < 3:
        print(
            "用法: python update_toml_from_requirements.py requirements.txt pyproject.toml [输出文件]"
        )
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
