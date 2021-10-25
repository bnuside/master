#!/usr/bin/env python3
import json
import os
import re
import subprocess


def get_test_packages(base_path):
    """
    :param base_path:
    :return:
        ['testcase.ios', 'testcase.ios.aaa']
    """
    packages: list[str] = []
    finnal_packages = []

    def __traverse(path):
        for f in os.listdir(path):
            ff = os.path.join(path, f)
            if os.path.isdir(ff) and "pycache" not in ff:
                packages.append(ff)
                __traverse(ff)
    __traverse(base_path)
    for p in packages:
        finnal_packages.append(p.replace("/", ".").replace("\\", "."))
    return finnal_packages


def __inner_filter_outputs(r_outputs):
    f_outputs = []
    for r_output in r_outputs:
        if not re.findall('(.*)#(.*)class', r_output) and not re.findall('(.*)#(.*)def', r_output):
            f_outputs.append(r_output)
    # print(f"f_outputs: {f_outputs}")
    return f_outputs


def __inner_slice_outputs(r_outputs):
    outputs = []
    temp = [r_outputs[0]]
    p = r_outputs[0].split(":")[0]
    for i in range(1, len(r_outputs)):
        if p == r_outputs[i].split(":")[0]:
            temp.append(r_outputs[i])
        else:
            outputs.append(temp)
            temp = [r_outputs[i]]
            p = r_outputs[i].split(":")[0]
    # print(f"outputs: {outputs}")
    return outputs


def better_parse_test_case(packages):

    cases = []
    if not packages:
        return cases

    for pk in packages:
        case = {"test_package": pk, "test_modules": []}
        pk = "/".join(pk.split("."))
        cmd = f"grep -e 'class .*(' -e 'def test_.*' -r {pk}/*.py"
        raw_outputs = subprocess.run(cmd,
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE,
                                     shell=True).stdout.decode("utf-8").split("\n")
        # print(f"raw_outputs: {raw_outputs}")
        filter_outputs = __inner_filter_outputs(raw_outputs)
        outputs = __inner_slice_outputs(filter_outputs)

        for o in outputs:
            item = {"test_module": re.findall(f'{pk}/(.*).py', o[0])[0],
                    "test_classes": []}

            outputs2 = []
            temp = [o[0]]
            for i in range(1, len(o)):
                if 'KRunner' not in o[i]:
                    temp.append(o[i])
                else:
                    outputs2.append(temp)
                    temp = [o[i]]
                if i == len(o) - 1:
                    outputs2.append(temp)

            for o2 in outputs2:
                item2 = {"test_class": re.findall(r'class(.*)\(', o2[0])[0].strip(),
                         "test_methods": []}
                methods = []
                if len(o2) > 1:
                    for i in range(1, len(o2)):
                        methods.append(re.findall(r'def(.*)\(', o2[i])[0].strip())
                item2["test_methods"] = methods
                item["test_classes"].append(item2)

            case["test_modules"].append(item)
        cases.append(case)
    # print('cases:\n' + json.dumps(cases, indent='   ', ensure_ascii=False))
    return cases


if __name__ == "__main__":
    test_packages = get_test_packages('testcase')
    android_packages = []
    ios_packages = []
    for package in test_packages:
        if "android" in package:
            android_packages.append(package)
        if 'ios' in package:
            ios_packages.append(package)

    result = {"project_key": "test", "case": {"android": [], "ios": []}}
    result["case"]["android"] = better_parse_test_case(android_packages)
    result["case"]["ios"] = better_parse_test_case(ios_packages)
    print('Result:\n' + json.dumps(result, indent='   ', ensure_ascii=False))