class AiStore:

    def __init__(self, st_name, st_id, st_locate):
        self.st_name = st_name
        self.st_id = st_id
        self.st_locate = st_locate
        self.p_count = 10
        self.p_price = 1000

    def buy_item(self, b_count, b_price):
        if self.p_count < b_count:
            print('재고가 부족합니다.')

        elif b_price < b_count * self.p_price:
            print('입력금액이 부족합니다')

        elif self.p_count >= b_count and b_price >= b_count * self.p_price:
            self.p_count = self.p_count - b_count
            print('잔돈은 ', b_price - b_count * self.p_price, '입니다')

        else:
            print('잘못된 입력입니다')


    def set_product(self, p_count, p_price):
        self.p_count = p_count
        self.p_price = p_price

    def get_name(self):
        return self.st_name

    def get_id(self):
        return self.st_id

    def get_locate(self):
        return self.st_locate

    def get_count(self):
        return self.p_count

    def get_price(self):
        return self.p_price


if __name__ == '__main__':

    st_name = input('스토어 지점이름 입력: ')
    st_id = input('스토어 지점번호 입력: ')
    st_locate = input('스토어 위치 입력: ')

    store = AiStore(st_name, st_id, st_locate)
    print(store.get_name() + ' 스토어가 생성 되었습니다.')


    for i in range(10):

        print('스토어 조회는 1번, 구매는 2번, 상품 관리는 3번, 종료는 4번 을 눌러주세요')
        num = input()
        if num == '1':
            print('지점이름 :', store.get_name())
            print('지점아이디 :', store.get_id())
            print('지점장소 :', store.get_locate())
            print('재고개수 :', store.p_count)
            print('상품가격 :', store.p_price)

        elif num == '2':
            count = int(input('구매할 상품 개수 입력'))
            need_price = count * store.p_price
            print('필요한 금액은', need_price, '입니다.')
            amount = int(input('지불 금액을 입력해 주세요'))
            store.buy_item(count, amount)

        elif num == '3':
            count = int(input('상품 재고 입력'))
            price = int(input('상품 가격 입력'))
            store.set_product(count, price)

        elif num == '4':
            print('종료합니다')
            break
        else:
            print('잘못된 입력입니다')