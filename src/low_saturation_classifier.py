# Author : Hyunwoong
# When : 6/19/2019
# Homepage : github.com/gusdnd852

from src.color_extractor import ColorExtractor


class LowSaturationClassifier:
    extractor = ColorExtractor()
    arr = []

    def is_gray(self, file, k=3):
        col, pr = self.extractor.get_color(file, 3) 
        arr = [i[1] for i in col]
        
        gfactor = 0
        for i in arr:
            gfactor += (abs(i[0] - i[1]))
            gfactor += (abs(i[1] - i[2]))
            gfactor += (abs(i[0] - i[2]))
        print('grayfactor is ' + str(gfactor))
        print('pearson cor. is ' + str(pr))
        if gfactor < 150 and np.min(pr) > 0.95:
            return True
        else:
            return False
