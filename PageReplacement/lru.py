from typing import List


def lru_cache(cache_size: int, page_call: List[int]) -> int:
    page_faults = 0

    if cache_size > 0:
        queue = []
        for page in page_call:
            if page not in queue:
                page_faults += 1
                if len(queue) >= cache_size:
                    queue.pop(0)

                queue.append(page)
            else:
                queue.remove(page)
                queue.append(page)
    else:
        # 캐시하지 않는다면 모든 페이지 호출이 페이지 부재임.
        page_faults = len(page_call)

    return page_faults


if __name__ == "__main__":
    pages = [1, 2, 1, 3, 2, 5, 7, 1, 8]
    cache_missed = lru_cache(cache_size=3, page_call=pages)
    print(cache_missed)
