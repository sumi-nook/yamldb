import re

from yamldb.auto_complete import AutoCompleteRunner
from yamldb.auto_complete.tasks.id import AutoCompleteIDTask


RE_UUID = re.compile(r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$")

def is_uuid(s):
    return bool(RE_UUID.match(s))


def test_add_new_id():
    tasks = [
        AutoCompleteIDTask(),
    ]
    runner = AutoCompleteRunner(tasks)
    data = [
        {},
    ]
    result = runner.apply(data)
    assert len(result) == 1
    assert "id" in result[0]


def test_existing_case():
    tasks = [
        AutoCompleteIDTask(),
    ]
    runner = AutoCompleteRunner(tasks)
    data = [
        {"id": "hoge"},
    ]
    result = runner.apply(data)
    assert len(result) == 1
    assert "id" in result[0]
    assert result[0]["id"] == "hoge"


def test_multi_items():
    tasks = [
        AutoCompleteIDTask(),
    ]
    runner = AutoCompleteRunner(tasks)
    data = [
        {},
        {"id": "hoge"},
        {"hoge": "fuga"},
    ]
    result = runner.apply(data)
    assert len(result) == 3
    assert "id" in result[0]
    assert is_uuid(result[0]["id"])
    assert "id" in result[1]
    assert result[1]["id"] == "hoge"
    assert "id" in result[2]
    assert is_uuid(result[2]["id"])
