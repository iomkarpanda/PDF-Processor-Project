import fitz

doc = fitz.open(r"C:\Users\Ajay kumar\Downloads\PDF Processor Project\sample.pdf")

toc = [
    [1, "HEAPS & PRIORITY QUEUES – Overview", 1],
    [1, "Super Pattern 1 — K-Selection Using Heap", 2],
    [1, "Super Pattern 2 — Greedy + Heap (Scheduling / Selection)", 3],
    [1, "Super Pattern 3 — Heap as Priority Queue in Graphs", 4],
    [1, "Super Pattern 4 — Merging & Stream Processing With Heaps", 5],
    [1, "Super Pattern 5 — Frequency & Buckets With Heap", 6],
    [1, "Super Pattern 6 & 7 — Intervals + Heap / Advanced Usage", 7],
]

doc.set_toc(toc)

doc.save("sample_with_toc.pdf")
doc.close()
