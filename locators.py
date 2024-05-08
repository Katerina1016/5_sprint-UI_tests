from selenium.webdriver.common.by import By


class MainPageLocators:  # Главная страница
    personal_account_but = (By.XPATH, ".//p[text() = 'Личный Кабинет']")  # кнопка – Личный кабинет
    login_account_but = (By.XPATH, ".//button[text() = 'Войти в аккаунт']")  # кнопка – Войти в аккаунт
    place_an_order_but = (By.XPATH, ".//button[text() = 'Оформить заказ']")  # кнопка – Оформить заказ
    list_of_sauces = (By.XPATH, ".//span[contains(text(),'Соусы')]")  # список - Соусы
    list_of_buns = (By.XPATH, ".//span[contains(text(),'Булки')]")  # cписок - Булки
    fillings_list = (By.XPATH, ".//span[contains(text(),'Начинки')]")  # cписок - Начинки
    active_tab_in_constructor = (By.XPATH, ".//div[contains(@class, 'current')]/span")  # Проверка активной вкладки


class AuthorizationPageLocators:  # страница «Авторизация и восстановление данных»
    email_input = (By.XPATH, ".//input[@name = 'name']")  # Поле ввода Email
    password_input = (By.XPATH, ".//input[@name = 'Пароль']")  # Поле ввода пароля
    login_account_auth_form_but = (By.XPATH, "//button[text() = 'Войти']")  # кнопка  - Войти


class RegistrationPageLocators:  # Страница «Регистрации логина»
    name_input = (By.XPATH, ".//label[text() = 'Имя']/following-sibling::input")  # Поле ввода имени
    email_input = (By.XPATH, ".//label[text() = 'Email']/following-sibling::input")  # Поле ввода Email
    password_input = (By.XPATH, ".//label[text() = 'Пароль']/following-sibling::input")  # Поле ввода пароля
    registration_but = (By.XPATH, ".//button[text() = 'Зарегистрироваться']")  # кнопка - Зарегистрироваться
    enter_but = (By.XPATH, ".//a[text() = 'Войти']")  # кнопка - Войти
    error_message_double_register = (By.XPATH, ".//p[text() = 'Такой пользователь уже существует']")
    # ошибка при попытке повторной регистрации
    error_message_incorrect_pass = (By.XPATH, ".//p[text() = 'Некорректный пароль']")
    # Ошибка при вводе некорректного пароля


class PasswordRecoverPageLocators:  # страница «Восстановления пароля»
    login_account_but = (By.XPATH, ".//a[text() = 'Войти']")  # кнопка - Войти


class PersonalAccountLocators:  # страница «Личный кабинет»
    exit_but = (By.XPATH, ".//button[text() = 'Выход']")  # кнопка - Выход
    save_but = (By.XPATH, ".//button[text() = 'Сохранить']")  # кнопка - Сохранить
    constructor_but = (By.XPATH, ".//p[text() = 'Конструктор']")  # кнопка  - Конструктор
    logo_but = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']")  # кнопка главной страницы сайта
