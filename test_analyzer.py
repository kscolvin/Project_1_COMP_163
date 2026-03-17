import pytest
import os
import sys

# Import the student's module
import analyzer

# ============================================================
# Shared test data used across most tests
# This data is controlled and known so assertions can be exact
# ============================================================

TEST_DATA = [
    {"title": "Alpha",   "year": "2018", "genre": "Action",  "rating": "8.5", "value": "150.0"},
    {"title": "Beta",    "year": "2019", "genre": "Comedy",  "rating": "6.2", "value": "80.0"},
    {"title": "Gamma",   "year": "2020", "genre": "Action",  "rating": "7.1", "value": "120.0"},
    {"title": "Delta",   "year": "2018", "genre": "Drama",   "rating": "9.0", "value": "200.0"},
    {"title": "Epsilon", "year": "2021", "genre": "Comedy",  "rating": "5.5", "value": "60.0"},
    {"title": "Zeta",    "year": "2019", "genre": "Drama",   "rating": "7.8", "value": "175.0"},
    {"title": "Eta",     "year": "2020", "genre": "Action",  "rating": "6.9", "value": "95.0"},
]


# ============================================================
# load_data() — 8 points
# Tests structure of returned data using the student's chosen
# dataset file. Does not assert exact values since each student
# chose a different dataset.
# ============================================================

class TestLoadData:

    def test_returns_list(self):
        """load_data should return a list"""
        result = analyzer.load_data(analyzer.DATASET)
        assert isinstance(result, list)

    def test_list_is_not_empty(self):
        """load_data should return at least one record"""
        result = analyzer.load_data(analyzer.DATASET)
        assert len(result) > 0

    def test_records_are_dicts(self):
        """Each record in the returned list should be a dictionary"""
        result = analyzer.load_data(analyzer.DATASET)
        assert isinstance(result[0], dict)

    def test_required_columns_present(self):
        """Each record should contain all required column names"""
        result = analyzer.load_data(analyzer.DATASET)
        required_columns = {"title", "year", "genre", "rating", "value"}
        assert required_columns.issubset(result[0].keys())


# ============================================================
# filter_data() — 8 points
# ============================================================

class TestFilterData:

    def test_returns_correct_rows(self):
        """filter_data should return only rows matching the given column and value"""
        result = analyzer.filter_data(TEST_DATA, "genre", "Action")
        assert len(result) == 3
        for row in result:
            assert row["genre"] == "Action"

    def test_no_extra_rows(self):
        """filter_data should not include rows that do not match"""
        result = analyzer.filter_data(TEST_DATA, "genre", "Comedy")
        for row in result:
            assert row["genre"] != "Action"
            assert row["genre"] != "Drama"

    def test_filter_by_year(self):
        """filter_data should work on any column, not just genre"""
        result = analyzer.filter_data(TEST_DATA, "year", "2018")
        assert len(result) == 2
        for row in result:
            assert row["year"] == "2018"

    def test_no_match_returns_empty_list(self):
        """filter_data should return an empty list when no rows match"""
        result = analyzer.filter_data(TEST_DATA, "genre", "Horror")
        assert result == []


# ============================================================
# get_category_stats() — 8 points
# ============================================================

class TestGetCategoryStats:

    def test_returns_three_values(self):
        """get_category_stats should return three values"""
        result = analyzer.get_category_stats(TEST_DATA, "rating")
        assert len(result) == 3

    def test_correct_minimum(self):
        """get_category_stats should return the correct minimum"""
        low, high, avg = analyzer.get_category_stats(TEST_DATA, "rating")
        assert low == 5.5

    def test_correct_maximum(self):
        """get_category_stats should return the correct maximum"""
        low, high, avg = analyzer.get_category_stats(TEST_DATA, "rating")
        assert high == 9.0

    def test_correct_average(self):
        """get_category_stats should return the correct average rounded to 2 decimal places"""
        low, high, avg = analyzer.get_category_stats(TEST_DATA, "rating")
        expected = round(sum(float(r["rating"]) for r in TEST_DATA) / len(TEST_DATA), 2)
        assert avg == expected


# ============================================================
# summarize() — 8 points
# ============================================================

class TestSummarize:

    def test_returns_dict(self):
        """summarize should return a dictionary"""
        result = analyzer.summarize(TEST_DATA)
        assert isinstance(result, dict)

    def test_total_records(self):
        """summarize should return the correct total record count"""
        result = analyzer.summarize(TEST_DATA)
        assert result["total_records"] == 7

    def test_unique_genres(self):
        """summarize should return the correct number of unique genres"""
        result = analyzer.summarize(TEST_DATA)
        assert result["unique_genres"] == 3

    def test_average_rating(self):
        """summarize should return the correct average rating rounded to 2 decimal places"""
        result = analyzer.summarize(TEST_DATA)
        expected = round(sum(float(r["rating"]) for r in TEST_DATA) / len(TEST_DATA), 2)
        assert result["average_rating"] == expected


# ============================================================
# display_summary() — 6 points
# ============================================================

class TestDisplaySummary:

    def test_runs_without_error(self):
        """display_summary should run without raising an exception"""
        try:
            analyzer.display_summary(TEST_DATA)
        except Exception as e:
            pytest.fail(f"display_summary raised an exception: {e}")

    def test_produces_output(self, capsys):
        """display_summary should print something to the console"""
        analyzer.display_summary(TEST_DATA)
        captured = capsys.readouterr()
        assert len(captured.out.strip()) > 0

    def test_returns_none(self):
        """display_summary should not return a value"""
        result = analyzer.display_summary(TEST_DATA)
        assert result is None


# ============================================================
# generate_insights() — 7 points
# ============================================================

class TestGenerateInsights:

    def test_returns_list(self):
        """generate_insights should return a list"""
        result = analyzer.generate_insights(TEST_DATA)
        assert isinstance(result, list)

    def test_at_least_three_insights(self):
        """generate_insights should return at least 3 insights"""
        result = analyzer.generate_insights(TEST_DATA)
        assert len(result) >= 3

    def test_insights_are_strings(self):
        """each insight should be a string"""
        result = analyzer.generate_insights(TEST_DATA)
        for insight in result:
            assert isinstance(insight, str)

    def test_insights_are_not_empty(self):
        """each insight string should be non-empty"""
        result = analyzer.generate_insights(TEST_DATA)
        for insight in result:
            assert len(insight.strip()) > 0


# ============================================================
# export_report() — 10 points
# ============================================================

class TestExportReport:

    def test_file_is_created(self, tmp_path):
        """export_report should create the output file"""
        output = tmp_path / "report.txt"
        analyzer.export_report(TEST_DATA, str(output))
        assert output.exists()

    def test_file_is_not_empty(self, tmp_path):
        """export_report should write content to the file"""
        output = tmp_path / "report.txt"
        analyzer.export_report(TEST_DATA, str(output))
        assert output.stat().st_size > 0

    def test_known_title_in_report(self, tmp_path):
        """export_report should include data from the dataset in the report"""
        output = tmp_path / "report.txt"
        analyzer.export_report(TEST_DATA, str(output))
        content = output.read_text()
        assert "Delta" in content  # highest rated entry in TEST_DATA

    def test_default_top_n(self, tmp_path):
        """export_report should include 5 entries by default"""
        output = tmp_path / "report.txt"
        analyzer.export_report(TEST_DATA, str(output))
        content = output.read_text()
        # The top 5 by rating are: Delta(9.0), Alpha(8.5), Zeta(7.8), Gamma(7.1), Eta(6.9)
        for title in ["Delta", "Alpha", "Zeta", "Gamma", "Eta"]:
            assert title in content

    def test_custom_top_n(self, tmp_path):
        """export_report should respect a custom top_n value"""
        output = tmp_path / "report.txt"
        analyzer.export_report(TEST_DATA, str(output), top_n=2)
        content = output.read_text()
        # Top 2 by rating are Delta (9.0) and Alpha (8.5)
        # Count how many of the 7 titles appear in the report
        all_titles = [r["title"] for r in TEST_DATA]
        titles_in_report = [t for t in all_titles if t in content]
        # Only 2 titles should appear since top_n=2
        assert len(titles_in_report) == 2
        assert "Delta" in titles_in_report
        assert "Alpha" in titles_in_report
