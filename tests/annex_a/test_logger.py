from sfdata_stream_parser import events

from liiatools.datasets.annex_a.lds_annexa_clean import (
    logger
)

list_1_columns = [
    "Child Unique ID",
    "Gender",
    "Ethnicity",
    "Date of Birth",
    "Age of Child (Years)",
    "Date of Contact",
    "Contact Source",
]


def test_duplicate_columns():
    columns_list = list_1_columns + ["Child Unique ID"]
    assert logger._duplicate_columns(columns_list) == ["Child Unique ID"]


def test_duplicate_columns_error():
    stream = logger.duplicate_column_check(
        [
            events.StartTable(matched_column_headers=list_1_columns + ["Child Unique ID"], sheet_name="List 1")
        ]
    )
    stream = list(stream)
    assert stream[0].duplicate_column_error == f"Sheet with title List 1 contained the following duplicate " \
                                               f"column(s): 'Child Unique ID'"

    stream = logger.duplicate_column_check(
        [
            events.StartTable(sheet_name="List 1")
        ]
    )
    stream = list(stream)
    assert stream[0] == events.StartTable(sheet_name="List 1")


def test_blank_error_check():
    stream = logger.blank_error_check(
        [
            events.Cell(other_config={"canbeblank": False}, value="", error="0"),
            events.Cell(other_config={"canbeblank": False}, value=None, error="0"),
            events.Cell(other_config={"canbeblank": False}, value="", error="1"),
            events.Cell(other_config={"canbeblank": False}, value="string", error="0"),
            events.Cell(other_config={"canbeblank": True}, value="", error="0"),
        ]
    )
    stream = list(stream)
    assert stream[0].blank_error == "1"
    assert stream[1].blank_error == "1"
    assert "blank_error" not in stream[2].as_dict()
    assert "blank_error" not in stream[3].as_dict()
    assert "blank_error" not in stream[4].as_dict()
