"""Tnie arkusz postaci 2x2 (idle, roar, walk1, walk2) na 4 pliki PNG z przezroczystym tłem.
Użycie:  python tools/cut_sheets.py assets/sheet_trex.png trex
         python tools/cut_sheets.py assets/skel_trex.png --single skel_trex   (jeden obrazek, tylko usuwa tło)
Wymaga: pip install pillow numpy
"""
import sys, os
import numpy as np
from PIL import Image

def remove_white(img, thresh=235, soft=40):
    a = np.asarray(img.convert('RGBA')).astype(np.int16)
    rgb = a[:, :, :3]
    mn = rgb.min(axis=2)
    # biel -> alfa 0, przejście miękkie
    alpha = np.clip((thresh - mn) * (255 / soft), 0, 255).astype(np.uint8)
    # obszar poza postacią: wypełnienie od krawędzi (żeby białe oczy zostały)
    from collections import deque
    h, w = alpha.shape
    outside = np.zeros((h, w), bool)
    q = deque()
    for x in range(w):
        for y in (0, h - 1):
            if alpha[y, x] < 128 and not outside[y, x]: outside[y, x] = True; q.append((y, x))
    for y in range(h):
        for x in (0, w - 1):
            if alpha[y, x] < 128 and not outside[y, x]: outside[y, x] = True; q.append((y, x))
    while q:
        y, x = q.popleft()
        for ny, nx in ((y-1,x),(y+1,x),(y,x-1),(y,x+1)):
            if 0 <= ny < h and 0 <= nx < w and not outside[ny, nx] and alpha[ny, nx] < 128:
                outside[ny, nx] = True; q.append((ny, nx))
    final = np.where(outside, alpha, 255).astype(np.uint8)
    out = a.copy(); out[:, :, 3] = final
    return Image.fromarray(out.astype(np.uint8), 'RGBA')

def crop_to_content(img, pad=20):
    bbox = img.getchannel('A').point(lambda v: 255 if v > 20 else 0).getbbox()
    if not bbox: return img
    l, t, r, b = bbox
    return img.crop((max(0, l-pad), max(0, t-pad), min(img.width, r+pad), min(img.height, b+pad)))

def main():
    args = sys.argv[1:]
    if not args: print(__doc__); return
    src = args[0]; img = Image.open(src)
    outdir = os.path.dirname(src) or '.'
    if '--single' in args:
        name = args[args.index('--single') + 1]
        crop_to_content(remove_white(img)).save(os.path.join(outdir, f'{name}.png')); print('zapisano', name); return
    prefix = args[1]
    w, h = img.size; cw, ch = w // 2, h // 2
    poses = ['idle', 'roar', 'walk1', 'walk2']
    for i, pose in enumerate(poses):
        x, y = (i % 2) * cw, (i // 2) * ch
        part = crop_to_content(remove_white(img.crop((x, y, x + cw, y + ch))))
        part.save(os.path.join(outdir, f'{prefix}_{pose}.png')); print('zapisano', f'{prefix}_{pose}.png', part.size)

if __name__ == '__main__': main()
