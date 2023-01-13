def jsonify(dictionary):
        returnString = "{"
        for key in dictionary.keys():
            returnString += '"'+key+'":'
            returnString += ('"' if dictionary[key][0] != "{" else "") +dictionary[key]+('",' if dictionary[key][-1]!="}" else ",")
        returnString = returnString[0:-1] + "}"
        return returnString
