import random

def fifo(page_ref, num_frames):
    frames = []
    page_faults = 0
    for page in page_ref:
        if page not in frames:
            if len(frames) < num_frames:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)
            page_faults += 1
    return page_faults

def lru(page_ref, num_frames):
    frames = []
    page_faults = 0
    page_order = []
    for page in page_ref:
        if page not in frames:
            if len(frames) < num_frames:
                frames.append(page)
                page_order.append(page)
            else:
                page_removed = page_order.pop(0)
                frames.remove(page_removed)
                frames.append(page)
                page_order.append(page)
            page_faults += 1
        else:
            page_order.remove(page)
            page_order.append(page)
    return page_faults

def generate_ref_page(size, num_pages):
    return [random.randint(0, num_pages - 1) for _ in range(size)]

page_ref = generate_ref_page(100, 10)

for num_frames in range(1, 11):
    faults_fifo = fifo(page_ref, num_frames)
    faults_lru = lru(page_ref, num_frames)
    print(f"Page Frames: {num_frames}, FIFO Page Faults: {faults_fifo}, LRU Page Faults: {faults_lru}")