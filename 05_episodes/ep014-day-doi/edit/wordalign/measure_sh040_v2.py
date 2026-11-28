import numpy as np
from PIL import Image
from scipy import ndimage

EP = "/home/hatch/workspace/gen-videos-for-affiliate-git/05_episodes/ep014-day-doi"
print("== sh040 take001: face centroid (YCrCb skin mask) + shoulder edge + cup ==")
print("frame 720x1280; face zone x150-500 y250-700; skin: Cr 133-173, Cb 77-127, Y>60")
for t in (1, 2, 4, 5.5, 7):
    im = Image.open(f"{EP}/edit/qc-frames/sh040-m{t}.png").convert("RGB")
    ycbcr = np.asarray(im.convert("YCbCr")).astype(int)
    Y, Cb, Cr = ycbcr[...,0], ycbcr[...,1], ycbcr[...,2]
    skin = (Cr>=133)&(Cr<=173)&(Cb>=77)&(Cb<=127)&(Y>60)
    zone = np.zeros_like(skin); zone[250:700, 150:500] = True
    m = skin & zone
    lab, n = ndimage.label(m)
    sizes = ndimage.sum_labels(m, lab, range(1, n+1))
    if n == 0 or sizes.max() < 200:
        print(f"t={t}: NO face blob"); continue
    k = int(np.argmax(sizes)) + 1
    ys, xs = np.where(lab == k)
    cx, cy = xs.mean(), ys.mean()
    print(f"t={t}: face blob {len(xs)}px bbox x{xs.min()}-{xs.max()} y{ys.min()}-{ys.max()} "
          f"centroid=({cx:.0f},{cy:.0f}) -> in v1 crop x0-440: {cx/440*100:.0f}% width")
    # shoulder left edge per 40px y-band, y270-1080: leftmost x in [380,720] with lum<70 run>=10px
    lum = np.asarray(im.convert("L")).astype(float)
    edges = []
    for y0 in range(270, 1080, 40):
        band = (lum[y0:y0+40, 380:720] < 70)
        colrun = band.mean(axis=0) > 0.5   # dark in >half the band height
        # first run of >=10 consecutive dark cols
        e = None
        run = 0
        for i, v in enumerate(colrun):
            run = run+1 if v else 0
            if run >= 10:
                e = 380 + i - 9
                break
        edges.append((y0, e))
    emin = min(e for _, e in edges if e is not None)
    print(f"     shoulder left edge per y-band: {[(y,e) for y,e in edges]}")
    print(f"     MIN shoulder edge over y270-1080: x={emin}")
    # cup: dark pixels lum<80 in x200-480, y800-1150
    cup = lum[800:1150, 200:480] < 80
    ys2, xs2 = np.where(cup)
    print(f"     cup/hand dark bbox: x{200+xs2.min()}-{200+xs2.max()} y{800+ys2.min()}-{800+ys2.max()}")
