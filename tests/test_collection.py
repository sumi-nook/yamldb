import io

from yamldb.collection import Collection
from yamldb.collection import CollectionQuery


TEST_DATA = [
    {"a": 1, "b": 2, "c": 3},
    {"a": 4, "b": 5, "c": 6},
    {"a": 7, "b": 8, "c": 9},
]


def test_collection_select_eq():
    collection = Collection(TEST_DATA)
    # ==
    query = CollectionQuery([
        ("a", "==", 1),
    ])
    result = collection.select(query)
    assert len(result) == 1
    assert result[0]["a"] == 1


def test_collection_select_ne():
    collection = Collection(TEST_DATA)
    # !=
    query = CollectionQuery([
        ("a", "!=", 1),
    ])
    result = collection.select(query)
    assert len(result) == 2
    assert result[0]["a"] == 4
    assert result[1]["a"] == 7


def test_collection_select_gt():
    collection = Collection(TEST_DATA)
    # >
    query = CollectionQuery([
        ("a", ">", 4),
    ])
    result = collection.select(query)
    assert len(result) == 1
    assert result[0]["a"] == 7


def test_collection_select_ge():
    collection = Collection(TEST_DATA)
    # >=
    query = CollectionQuery([
        ("a", ">=", 4),
    ])
    result = collection.select(query)
    assert len(result) == 2
    assert result[0]["a"] == 4
    assert result[1]["a"] == 7


def test_collection_select_lt():
    collection = Collection(TEST_DATA)
    # >
    query = CollectionQuery([
        ("a", "<", 4),
    ])
    result = collection.select(query)
    assert len(result) == 1
    assert result[0]["a"] == 1


def test_collection_select_le():
    collection = Collection(TEST_DATA)
    # >=
    query = CollectionQuery([
        ("a", "<=", 4),
    ])
    result = collection.select(query)
    assert len(result) == 2
    assert result[0]["a"] == 1
    assert result[1]["a"] == 4


def test_collection_load_save():
    data = """
- a: 1
  b: 2
  c: 3
- a: 4
  b: 5
  c: 6
    """.strip()
    fileobj = io.StringIO(data)
    collection = Collection.load(fileobj)
    query = CollectionQuery([
        ("a", "==", 1),
    ])
    result = collection.select(query)
    assert len(result) == 1
    assert result[0]["a"] == 1

    fileobj = io.StringIO()
    collection.save(fileobj)
    fileobj.seek(0)
    test = fileobj.read().strip()
    assert data == test
