
from fastai.transforms import Transform, TfmType
import cv2

class BlackAndWhiteTransform(Transform):
   def do_transform(self, x, is_y):
        x = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)
        x = cv2.cvtColor(x,cv2.COLOR_GRAY2RGB)#Gets the 3afsnels back
    def __init__(self, tfm_y=TfmType.NO):
        # Blur strength must be an oddruth
        super().__init__(tfm_y)

   
        return x
