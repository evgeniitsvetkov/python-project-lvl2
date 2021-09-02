from gendiff import generator, parser


def test_make_plain_tree():
	file_path1 = 'tests/fixtures/file1.json'
	file_path2 = 'tests/fixtures/file2.json'
	data1 = parser.load_data(file_path1)
	data2 = parser.load_data(file_path2)

	diff_repr = [
	('follow', False, None), 
	('host', 'hexlet.io', 'hexlet.io'), 
	('proxy', '123.234.53.22', None), 
	('timeout', 50, 20), 
	('verbose', None, True)
	]

	assert generator.make_tree(data1, data2) == diff_repr


def test_plain_json():
	file_path1 = 'tests/fixtures/file1.json'
	file_path2 = 'tests/fixtures/file2.json'

	with open('tests/fixtures/diff.txt') as f:
		data = f.read()

	assert generator.generate_diff(file_path1, file_path2) == data


def test_plain_yaml():
	file_path1 = 'tests/fixtures/file1.yaml'
	file_path2 = 'tests/fixtures/file2.yml'

	with open('tests/fixtures/diff.txt') as f:
		data = f.read()

	assert generator.generate_diff(file_path1, file_path2) == data
