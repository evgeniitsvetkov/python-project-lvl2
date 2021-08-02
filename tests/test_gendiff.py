from gendiff import generator


def test_plain_json():
	file_path1 = 'tests/fixtures/file1.json'
	file_path2 = 'tests/fixtures/file2.json'

	with open('tests/fixtures/diff.txt') as f:
		data = f.read()

	assert generator.generate_diff(file_path1, file_path2) == data
