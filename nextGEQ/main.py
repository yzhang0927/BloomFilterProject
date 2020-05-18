# 

'''
    void next_geq(std::uint32_t docid)
    {
        if (documents[0] < max_docid) {
            auto new_pos = std::lower_bound(documents.begin(), documents.end(), docid);
            auto skip = std::distance(documents.begin(), new_pos);
            documents = documents.subspan(skip);
            frequencies = frequencies.subspan(skip);
            try_finish();
        }
    }
'''

def readData(fileName): 
    f = open(fileName, "r")
    if f.mode == "r": 
        contents = f.read()
        # print(contents)
        return contents
    f.close()

def generateRandomInput(lstOfKnownPositives, percentageOfPositve, size, lowerBound, upperBound): 
    


def main(): 
    data = readData("inverted_index_list.txt")

    listOfIndexes = data.split(" ")
    for item in listOfIndexes: 
        print(item)


if __name__ == '__main__':
    main()

# 1. read data 
# 2. split the data into trunks
# 3. record the max in each chunk
# 4. 