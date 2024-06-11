import allure

from pages.base_pade import BasePage
from locators import MainPageLocators
from seletools.actions import drag_and_drop


class MainPage(BasePage):

    @allure.step('Дождаться загрузки главной страницы')
    def loading_main_page(self):
        return self.find_element_located(MainPageLocators.MAIN_PAGE)

    @allure.step('Перейти в личный кабинет')
    def click_on_personal_cabinet_button(self):
        return self.find_element_clickable(MainPageLocators.PERSONAL_ACC_BUTTON)

    @allure.step('Нажать на кнопку "Оформить заказ"')
    def click_on_order_button(self):
        return self.find_element_clickable(MainPageLocators.ORDER_BUTTON)

    @allure.step('Перейти к конструктору')
    def click_on_constructor_button(self):
        return self.find_element_clickable(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Найти хедер "Соберите бургер"')
    def make_order_is_showing(self):
        return self.find_element_located(MainPageLocators.MAKE_ORDER_HEADER)

    @allure.step('Перейти к ленте заказов')
    def click_on_order_feed_button(self):
        return self.find_element_clickable(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step('Нажать на ингредиент')
    def click_on_ingredient(self):
        return self.find_element_clickable(MainPageLocators.BURGER_NAME)

    @allure.step('Дождаться открытия модального окна с информацией об ингредиенте')
    def opening_ingredient_details_window(self):
        return self.find_element_located(MainPageLocators.INGREDIENT_DETAILS_HEADER)

    @allure.step('Закрыть модальное окна с информацией об ингредиенте')
    def click_close_modal_window_button(self):
        return self.find_element_clickable(MainPageLocators.CLOSE_MODAL_WINDOW_BUTTON)

    @allure.step('Дождаться закрытия модального окна с информацией об ингредиенте')
    def wait_for_modal_window_closing(self):
        return self.wait_for_invisible(MainPageLocators.CLOSE_MODAL_WINDOW_BUTTON)

    @allure.step('Добавить ингредиент в корзину')
    def put_ingredient_into_basket(self, ingredient_name):
        ingredient = self.find_element_located(ingredient_name)
        basket = self.find_element_located(MainPageLocators.BASKET)
        drag_and_drop(self.driver, ingredient, basket)

    @allure.step('Получить кол-во ингредиента в корзине')
    def get_ingredients_number(self):
        num = self.find_element_located(MainPageLocators.INGREDIENT_COUNTER).text
        return int(num)

    @allure.step('Дождаться открытия модального окна с информацией о заказе')
    def opening_order_model_window(self):
        return self.find_element_located(MainPageLocators.ORDER_MODAL_WINDOW)

    @allure.step('Получить номер заказа')
    def get_order_number(self):
        return self.find_element_located(MainPageLocators.ORDER_NUMBER).text

    @allure.step('Сделать заказ')
    def make_an_order(self):
        self.put_ingredient_into_basket(MainPageLocators.BURGER_NAME)
        self.put_ingredient_into_basket(MainPageLocators.SAUCE_NAME)
        self.click_on_order_button()
        self.opening_order_model_window()
        order_number = self.get_order_number()
        self.click_close_modal_window_button()
        return order_number

    @allure.step('Дождаться появления номера заказа в модальном окне')
    def wait_changing_order_number(self):
        self.waiting_for_text_changed(MainPageLocators.ORDER_NUMBER, '7')

