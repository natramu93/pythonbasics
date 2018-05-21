class JustCounter:
    __secretCount = 0

    def count(self):
        self.__secretCount += 1
        print(self.__secretCount)


counter = JustCounter()
counter.count()
counter.count()
#print(counter.__secretCount)
#_classname__instance
print (counter._JustCounter__secretCount)