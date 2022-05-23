# Contact: limemimorinn@gmail.com
# If you find any errors, or if you write better code, please email me.
from typing import List


def get_subtotal(source: List[int], target: int) -> List[List[int]]:

    result: List[List[int]] = []
    start = end = 0
    subtotal = 0

    while True:
        # 시작 포인터와 종료 포인터가 모두 배열의 끝에 도달했으면 루프를 종료.
        if start == end == len(source):
            break

        # 종료 포인터가 더 증가할 수 있을 때
        if end < len(source):

            # 부분합과 목표가 같은 경우 결과에 추가.
            if subtotal == target:
                result.append(source[start:end])

            # 부분합이 결과보다 작으면 아직 더 더해야 하므로 종료포인터를 증가시키고 부분합에 더한다.
            if subtotal < target:
                end += 1
                subtotal += source[start:end][-1]
            # 부분합이 결과보다 크거나 같으면 더 더해봤자 영원히 목표에 도달하지 못하므로 빼야 한다.
            # 시작 포인터를 증가시키고 부분합에서 뺀다.
            else:
                start += 1
                subtotal -= source[0:start][-1]
        # 종료 포인터가 배열의 끝에 도달했을 때에는 시작 포인터만 계속 증가시키며 부분합에서 값을 뺀다.
        else:
            start += 1
            subtotal -= source[0:start][-1]

            # 그러는 와중에 목표와 부분합이 일치하면 결과에 추가한다.
            if subtotal == target:
                result.append(source[start:end])

    return result


def get_subtotal_v2(source: List[int], target: int) -> List[List[int]]:
    # end가 배열의 끝일 때 subtotal >= target이면 start를 더 줄일 여지가 있다.
    # subtotal < target이면 더 이상 탐색해도 의미가 없다. 더 증가할 여지는 없고 빠지기만 하는데 이미 작으니까.
    # start, end 증가 조건이 end가 배열 끝일 때 탐색을 더 할 지 말지를 정하는 조건과 동일하므로 같은 분기에서 비교한다.

    result: List[List[int]] = []
    start = end = 0
    subtotal = 0

    while True:
        # start, end는 배열의 길이를 초과할 수 없다.
        # 따라서 먼저 start를 올리는 조건을 체크한 후
        if subtotal >= target:
            subtotal -= source[start]
            start += 1

        # end가 배열의 끝인지를 확인한다.
        elif end == len(source):
            break

        # 마지막으로 end를 증가시키는 경우를 체크한다.
        elif subtotal < target:
            subtotal += source[end]
            end += 1

        if subtotal == target:
            result.append(source[start:end])

    return result


if __name__ == "__main__":

    source1 = [i for i in range(1, 6)]
    result1 = get_subtotal(source1, 5)
    print(result1)
    # [[2, 3], [5]]

    source2 = [i for i in range(1, 11)]
    result2 = get_subtotal(source2, 22)
    print(result2)
    # [[4, 5, 6, 7]]

    source3 = [5, 3, 7, 2, 9, 11, 4, 6, 2]
    result3 = get_subtotal(source3, 11)
    print(result3)
    # [[2, 9], [11]]

    source4 = [i for i in range(1, 6)]
    result4 = get_subtotal_v2(source4, 5)
    print(result4)

    source5 = [i for i in range(1, 11)]
    result5 = get_subtotal_v2(source5, 22)
    print(result5)

    source6 = [5, 3, 7, 2, 9, 11, 4, 6, 2]
    result6 = get_subtotal_v2(source6, 11)
    print(result6)
