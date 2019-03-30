"""
search_directory.py

Searches files under directory for query
"""
import argparse
import os


def search_directory(directory, query):
    """
    Searches files under directory for query

    Arguments:
        directory: String, The full path of the directory to search
        query: String, The string to query from directory

    Returns:
        Array of strings, An array of absolute file paths that match the query
    """
    # Gather directory content
    index = _parse_directory(directory)
    # Search for query in content
    results = {}
    for key in index:
        value = 0
        # search file for occurences of query
        for word, count in index[key].iteritems():
            # Get number of times query in key
            strings = word.split(query)
            num_occurences = len(strings) - 1
            # multiply previous value by count
            value += num_occurences * count
        # save value of query
        if value > 0:
            results[key] = value
    # Sort by descending query value then by file names
    # https://stackoverflow.com/questions/9919342/sorting-a-dictionary-by-value-then-key#9919379
    return [v[0] for v in
            sorted(results.iteritems(), key=lambda(k, v): (-v, k))]


def _parse_directory(directory):
    """
    Scan a directory parsing the file name and file content

    Arguments:
        directory: String, the directory to scan

    Returns:
        mapping of files to number of occurences of words
    """
    result = {}
    for root, _, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            word_count = {file_name: 1}
            with open(file_path, 'r') as input_file:
                for line in input_file:
                    words = line.split()
                    for word in words:
                        if word not in word_count:
                            word_count[word] = 0
                        word_count[word] += 1
            result[file_path] = word_count
    return result


if __name__ == "__main__":
    # Pass parameters down to search_directory
    description = 'Searches specified directory for specified query'

    parser = argparse.ArgumentParser(
        description=description,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("directory")
    parser.add_argument("query")
    args = parser.parse_args()
    ret = search_directory(args.directory, args.query)
    if ret:
        print("\n".join(ret))
