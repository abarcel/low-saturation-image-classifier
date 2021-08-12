# Low-Saturation-Image-Classifier
Use the K Means algorithm, one of the machine learning techniques, to classify whether the image has low saturation or not.
Set the value of k to 3 to extract the three colors representing the whole image. Then, compare the RGB values of the three colors. If the RGB values are similar, they are classified as a grayscale image.
<br><br><br>

## 1. Gray Factor

Gray Factor is the basis of comparison. Add the absolute values ​​of R-G, R-B and G-B in all three colors representing the image. There are 3 values ​​per color and 9 values ​​are output. When all these values ​​are added, if it is over 125, it is classified as a color image. If it is lower than 125, it is classified as a grayscale.
<br><br><br>

## 2. Test

## 2-1. Color Image

<img width=256 height=256 src=https://user-images.githubusercontent.com/38183241/59990475-42aa1800-967e-11e9-93a9-8e32d5b528cf.jpg></img>
<br> grayfactor is 470.52425788922085
<br>pearson cor. is [0.998301149806383, 0.9544225578598304, 0.9558806487616031]
<br> this image is color image
<br><br>

<img width=256 height=256 src=https://user-images.githubusercontent.com/38183241/59990477-4342ae80-967e-11e9-8491-184ededa2a64.jpg></img>
<br> grayfactor is 220.43568655620754
<br>pearson cor. is [0.9743563488684338, 0.7793225276536758, 0.771329457201492]
<br> this image is color image
<br><br>

<img width=256 height=256 src=https://user-images.githubusercontent.com/38183241/59990478-4342ae80-967e-11e9-99cd-37a3ab855188.jpg></img>
<br> grayfactor is 342.6747186046876
<br>pearson cor. is [0.8463003359611176, 0.24013229951921455, 0.5094333222537719]
<br> this image is color image
<br><br>

<img width=256 height=256 src=https://user-images.githubusercontent.com/38183241/59990479-4342ae80-967e-11e9-8978-ffb537da597e.jpg></img>
<br> grayfactor is 394.7282865434952
<br>pearson cor. is [0.8842347669134358, 0.6019107452351065, 0.804053400978107]
<br> this image is color image
<br><br>

<img width=256 height=256 src=https://user-images.githubusercontent.com/38183241/59990480-4342ae80-967e-11e9-9f69-8c1f7b07bc1f.jpg></img>
<br> grayfactor is 657.7464599326447
<br>pearson cor. is [0.7563260170307213, -0.23820125137316528, 0.3830616741551697]
<br> this image is color image
<br><br>

<img width=256 height=256 src=https://user-images.githubusercontent.com/38183241/59990481-43db4500-967e-11e9-968f-b927de583f0b.jpg></img>
<br> grayfactor is 206.00782907707645
<br>pearson cor. is [0.9943596471323646, 0.9674622790523751, 0.9863348539010278]
<br> this image is color image
<br><br>

<img width=256 height=256 src=https://user-images.githubusercontent.com/38183241/59990482-43db4500-967e-11e9-903e-11251459caf9.jpg></img>
<br> ggrayfactor is 175.6815997487255
<br>pearson cor. is [0.9232897489689218, 0.7110867320266192, 0.9038129624777497]
<br> this image is color image
<br><br>

<img width=256 height=256 src=https://user-images.githubusercontent.com/38183241/59990483-43db4500-967e-11e9-9bc3-7f0461afcebf.jpg></img>
<br> grayfactor is 220.27850364338437
<br>pearson cor. is [0.9018057015067888, 0.5793870068450852, 0.7882215183511263]
<br> this image is color image
<br><br>

<img width=256 height=256 src=https://user-images.githubusercontent.com/38183241/59990484-43db4500-967e-11e9-9096-fb5dedc5493e.jpg></img>
<br> grayfactor is 120.10458316902202
<br>pearson cor. is [0.9637373959019013, 0.8673121014146177, 0.9578006374292347]
<br> this image is grayscale image
<br><br>

<img width=256 height=256 src=https://user-images.githubusercontent.com/38183241/59990485-4473db80-967e-11e9-8370-63901208b31e.jpg></img>
<br> grayfactor is 166.31362455905872
<br>pearson cor. is [0.9076417249719372, 0.6432873046527954, 0.8752785489282381]
<br> this image is color image
<br><br><br>

## 2-2. Low Saturation Image

<img width=256 height=256 src=https://user-images.githubusercontent.com/38183241/59990709-32466d00-967f-11e9-8f1e-6f51c857100c.jpg></img>
<br> grayfactor is 74.21911310598648
<br>pearson cor. is [0.992704417424682, 0.9695555365507498, 0.9869966284427292]
<br> this image is grayscale image
<br><br>

<img width=256 height=256 src=https://user-images.githubusercontent.com/38183241/59990710-32df0380-967f-11e9-8030-c412d201aeff.jpg></img>
<br> grayfactor is 17.075588341166053
<br>pearson cor. is [0.9964900324314341, 0.9840715187237231, 0.9928650499003064]
<br> this image is grayscale image
<br><br>

<img width=256 height=256 src=https://user-images.githubusercontent.com/38183241/59990711-32df0380-967f-11e9-89c6-25e0d4e154dd.jpg></img>
<br> grayfactor is 74.88695018349537
<br>pearson cor. is [0.9980980984374296, 0.9940754017831728, 0.9968755445148195]
<br> this image is grayscale image
<br><br>

<img width=256 height=256 src=https://user-images.githubusercontent.com/38183241/59990712-32df0380-967f-11e9-8aaf-b5b707c56edb.jpg></img>
<br> grayfactor is 21.33539739491391
<br>pearson cor. is [0.9951757619321523, 0.9863360507389254, 0.9955738275514766]
<br> this image is grayscale image
<br><br>

<img width=256 height=256 src=https://user-images.githubusercontent.com/38183241/59990713-32df0380-967f-11e9-913f-2530dfc8768e.jpg></img>
<br> grayfactor is 39.48300619984974
<br>pearson cor. is [0.9922463763018505, 0.9684718277757628, 0.9889113243156182]
<br> this image is grayscale image
<br><br>

<img width=256 height=256 src=https://user-images.githubusercontent.com/38183241/59990715-33779a00-967f-11e9-939c-5a68fba98691.jpg></img>
<br> grayfactor is 83.96907117104513
<br>pearson cor. is [0.9924595432619552, 0.9746555435085433, 0.9899383285110394]
<br> this image is grayscale image
<br><br>

<img width=256 height=256 src=https://user-images.githubusercontent.com/38183241/59990716-33779a00-967f-11e9-81c0-194b424e3be0.jpg></img>
<br> grayfactor is 50.63058456916559
<br>pearson cor. is [0.9914405627256, 0.9840449179418124, 0.9949326236794115]
<br> this image is grayscale image
<br><br>

<img width=256 height=256 src=https://user-images.githubusercontent.com/38183241/59990717-33779a00-967f-11e9-85b5-36499b40d85d.jpg></img>
<br> grayfactor is 29.323493394551207
<br>pearson cor. is [0.9948506162049093, 0.9900380307718722, 0.9947732483294935]
<br> this image is grayscale image
<br><br>

<img width=256 height=256 src=https://user-images.githubusercontent.com/38183241/59990718-33779a00-967f-11e9-8783-ab795236e50b.jpg></img>
<br> grayfactor is 44.287362059370594
<br>pearson cor. is [0.9986772691717005, 0.9957424900742402, 0.9978939263210007]
<br> this image is grayscale image
<br><br>

<img width=256 height=256 src=https://user-images.githubusercontent.com/38183241/59990719-34103080-967f-11e9-8cdd-476a6bec6a06.jpg></img>
<br> grayfactor is 30.095373834334453
<br>pearson cor. is [0.9947072740403489, 0.9805179391412833, 0.9922522251581154]
<br> this image is grayscale image
<br><br>

## 2-3. Test Accuracy

The test resulted in 20 images classification is correct out of a total of 20 images. An accuracy of 100% indicates that this classifier works correctly. 
<br><br>

