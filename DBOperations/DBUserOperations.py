from pymongo import MongoClient

class DBUser :
    def __init__(self):
        self.cluster = MongoClient("") #Place the API Key from the MongoDB Atlas Cluster Here
        self.db = self.cluster["ReviewCloneProject"]
        self.userAuthentication = self.db["UserAuthentication"]
        self.userDetails = self.db["UserDetails"]
        self.companies = self.db["Companies"]
        self.places = self.db["Places"]
        self.companyReviews = self.db["CompanyReviews"]
        self.placeReviews = self.db["PlaceReviews"]
        self.query = dict()
        self.subquery = dict()
        self.colquery = dict()

    def insertUser(self, user):
        userdict1 = dict()
        userdict2 = dict()
        userdict1['Username'] = user['Username']
        userdict1['Password'] = user['Password']

        userdict2['Name'] = user['Name']
        userdict2['Username'] = user['Username']
        userdict2['Country'] = user['Country']
        print('Inserting User')
        self.userAuthentication.insert_one(userdict1)
        self.userDetails.insert_one(userdict2)

    def searchUsernames(self) :
        self.query.clear()
        self.query['Username'] = 1
        print('Fetching User Details')
        result = self.userAuthentication.find({}, self.query)
        return [x['Username'] for x in result]

    def getPassword(self, user) :
        self.query.clear()
        self.subquery.clear()
        self.subquery['$eq'] = user
        self.query['Username'] = self.subquery
        self.colquery['Password'] = 1
        result = self.userAuthentication.find(self.query, self.colquery)
        try:
            return result[0]['Password']
        except IndexError:
            return -1

    def insertCompany(self, companyDetails):
        self.companies.insert_one(companyDetails)

    def insertPlace(self, placeDetails):
        self.places.insert_one(placeDetails)

    def fetchCompanyReviewByName(self, companyName):
        self.query.clear()
        self.subquery.clear()
        self.subquery['$regex'] = companyName
        self.query['Name'] = self.subquery
        result = self.companies.find(self.query)
        resultlist = list()
        for x in result :
            del x['_id']
            resultlist.append(x)
        return resultlist

    def fetchCompanyReviewByLocation(self, companyLocation):
        self.query.clear()
        self.subquery.clear()
        self.subquery['$regex'] = companyLocation
        self.query['Address'] = self.subquery
        result = self.companies.find(self.query)
        resultlist = list()
        for x in result :
            del x['_id']
            resultlist.append(x)
        return resultlist

    def fetchPlaceReviewByName(self, placeName):
        self.query.clear()
        self.subquery.clear()
        self.subquery['$regex'] = placeName
        self.query['Name'] = self.subquery
        result = self.places.find(self.query)
        resultlist = list()
        for x in result :
            del x['_id']
            resultlist.append(x)
        return resultlist

    def fetchPlaceReviewByLocation(self, placeLocation):
        self.query.clear()
        self.subquery.clear()
        self.subquery['$regex'] = placeLocation
        self.query['Address'] = self.subquery
        result = self.places.find(self.query)
        resultlist = list()
        for x in result :
            del x['_id']
            resultlist.append(x)
        return resultlist

    def fetchCompanyNames(self, companyName):
        self.query.clear()
        self.subquery.clear()
        self.subquery['$regex'] = companyName
        self.query['Name'] = self.subquery
        result = self.companies.find(self.query)
        try :
            resultlist = list()
            for i in result :
                resultlist.append(i['Name'])
            return resultlist
        except IndexError :
            return -1

    def fetchPlaceNames(self, placeName):
        self.query.clear()
        self.subquery.clear()
        self.subquery['$regex'] = placeName
        self.query['Name'] = self.subquery
        result = self.places.find(self.query)
        try:
            resultlist = list()
            for i in result :
                resultlist.append(i['Name'])
            return resultlist
        except IndexError:
            return -1

    def insertCompanyReview(self, companyReview):
        self.companyReviews.insert_one(companyReview)

    def insertPlaceReview(self, placeReview):
        self.placeReviews.insert_one(placeReview)

    def getAverageCompanyRating(self, filter, company):
        if filter == 'Location' :
            company = self.companies.find({'Address' : {'$eq' : company}})
            try :
                company = company[0]['Name']
            except IndexError :
                return 0
        self.query.clear()
        self.subquery.clear()
        self.subquery['$eq'] = company
        self.query['Name'] = self.subquery
        result = self.companyReviews.find(self.query)
        try:
            resultlist = list()
            for i in result:
                resultlist.append(i['Rating'])
            try :
                return int(sum(resultlist)/len(resultlist))
            except ZeroDivisionError :
                return 0
        except IndexError:
            return 0

    def getAveragePlaceRating(self, filter, place):
        if filter == 'Location' :
            place = self.places.find({'Address' : {'$eq' : place}})
            try :
                place = place[0]['Name']
            except IndexError :
                return 0
        self.query.clear()
        self.subquery.clear()
        self.subquery['$eq'] = place
        self.query['Name'] = self.subquery
        result = self.placeReviews.find(self.query)
        try:
            resultlist = list()
            for i in result:
                resultlist.append(i['Rating'])
            try :
                return int(sum(resultlist)/len(resultlist))
            except ZeroDivisionError :
                return 0
        except IndexError:
            return 0

    def fetchCompanyReviews(self, companyName):
        self.query.clear()
        self.subquery.clear()
        self.subquery['$regex'] = companyName
        self.query['Name'] = self.subquery
        result = self.companyReviews.find(self.query)
        resultlist = list()
        for x in result :
            del x['_id']
            resultlist.append(x)
        if len(resultlist) > 0:
            return resultlist
        return -1


    def fetchPlaceReviews(self, placeName):
        self.query.clear()
        self.subquery.clear()
        self.subquery['$regex'] = placeName
        self.query['Name'] = self.subquery
        result = self.placeReviews.find(self.query)
        resultlist = list()
        for x in result :
            del x['_id']
            resultlist.append(x)
        if len(resultlist) > 0:
            return resultlist
        return -1

