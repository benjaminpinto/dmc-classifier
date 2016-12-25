from src.metrics import distance_euclid


class DMC:
    def __init__(self):
        self.centroids = []
        self.classes = set()

    def run(self, sample, dataset):
        count_classified_correctly = 0
        self.build_centroids(dataset)

        for s in sample:
            Xnew = s[:(len(s) - 1)]  # unknown class
            Xnear = []
            near_distance = 0

            for c in self.centroids:
                distance = distance_euclid(Xnew, c)

                if distance <= near_distance or near_distance == 0:
                    near_distance = distance
                    Xnear = c
                else:
                    continue

            if s[len(s) - 1] == Xnear[len(Xnear) - 1]:
                print('success')
                print("sample  ", s)
                print("centroid", Xnear)
                print("distance", near_distance)
                print("-")
                count_classified_correctly += 1
                # self.update_centroid(s, len(sample))
            else:
                print('fail')
                print("sample  ", s)
                print("centroid", Xnear)
                print("distance", near_distance)
                print("-")
                continue

            # print(s)
            # print(Xnear)

        print("")
        print("Classified     : ", len(sample))
        print("Correct        : ", count_classified_correctly)
        print("Sucess rate (%): ", (count_classified_correctly * 100) / len(sample))


    def update_centroid(self, s, sampleSize):
        a = 1 / (sampleSize + 1)

        for c in self.centroids:
            if c[len(c) - 1] == s[len(s) - 1]:
                c = sum(self.dot_product((1 - a), c), self.dot_product(a, s))
                # c = self.dot_product((1 - a), c) + self.dot_product(a, s)


    def sum_vectors(self, vec1, vec2):
        vec = []

        for position in range(0, len(vec1) - 1):
            vec.append(vec1[position] + vec2[position])

        return vec


    def dot_product(self, scalar, vector):
        for position in range(0, len(vector) - 1):
            vector[position] = float(vector[position]) * scalar

        return vector


    def build_centroids(self, dataset):
        sizeClasses = len(self.classes)

        for d in dataset:
            self.classes.add(d[len(d) - 1])

            if len(self.classes) > sizeClasses: # instance added. class didnt existed
                sizeClasses = len(self.classes)
                self.centroids.append(d)
            else:
                self.compound_centroids(d)

        for c in self.classes:
            classOcurrency = 0

            for d in dataset:
                if c == d[len(d) - 1]:
                    classOcurrency += 1

            self.divide_centroids(c, classOcurrency)


    def divide_centroids(self, c, classOcurrency):
        for centroid in self.centroids:
            if centroid[len(centroid) - 1] == c:
                for position in range(0, (len(centroid) - 1)):
                    centroid[position] = centroid[position] / classOcurrency

    def compound_centroids(self, d):
        for c in self.centroids:
            if d[len(d) - 1] == c[len(c) - 1]:
                for position in range (0, (len(c) - 1)):
                    c[position] = float(c[position]) + float(d[position])