# Web Automation Framework

This is a project designed to minimize the setup and config of selenium and actions performed on elements

To use this library, create a snippet like below and populate the actions in the `run` method (remove the `pass` keyword)

```python
from web_automation.framework import Framework, Browser, By

class CustomClass(Framework):
    def run(self):
        pass

CustomClass(
    browser=Browser.CHROME,
    wait=10,
    headless=False,
    download_path=''
)
```

The Constructor accepts 4 params (only one mandatory: browser) which is applied across the automation session
- `browser: Browser` - The type of browser that you want to use, based on the [`Browser`](#browser-class) class
- `wait: int` - The wait time for an element before throwing `NoSuchElementException` exception, default value is `30` seconds
- `headless: bool` - Boolean option to set the automation to use the browser in headless mode (runs in background and no visible browser window), default value is `False`
- `download-path: str` - the path to store the downloaded files, default value is the system download folder

---

### Browser Class

The `Browser` enum from the module will provide the target browser required to run the automation.

The supported browsers are
- Google Chrome
- Microsoft Edge
- Mozilla Firefox
- Safari

---

### Element selection

The HTML elements in the browser can be selected using one of the below attributes

- id
- name
- tag name
- class name
- css selector
- xpath
- link text
- partial link text

These selectors are provided using the `By` class (Selenium Class)

---

### SelectBy Class

There are different ways to select an option in the dropdown menu. The `SelectBy` enum has the below listed options to select the item in the dropdown

- Index
- Text
- Value

---

### Actions Available

The below methods are available in the Framework Class and should be used inside the run method prefixing `self.`


- `type(elem_type, elem_id, value, clear)` - used to type the `value` in the element
  - `elem_type: By` - one of the options from `By`
  - `elem_id: str` - element ID value based on the `elem_type`
  - `value: str` - value to be typed in the component
  - `clear: bool` - Boolean value to clear the element before typing


- `click(elem_type, elem_id)` - used to click the element
  - `elem_type: By` - one fo the options from `By`
  - `elem_id: str` - element ID value based on the `elem_type`


- `select(elem_type, elem_id, select_by, value)` - used to select an options from the dropdown input
  - `elem_type: By` - one of the options from `By`
  - `elem_id: str` - element ID value based on the `elem_type`
  - `select_by: SelectBy` - one of the options from `SelectBy`
  - `value: str` - value for the `SelectBy` option type


- `deselect(elem_type, elem_id)` - used to deselect a dropdown list
  - `elem_type: By` - one of the options from `By`
  - `elem_id: str` - element ID value based on the `elem_type`


- `check_if_exists(elem_type, elem_id)` - used to check if the mentioned element exists in the page
  - `elem_type: By` - one of the options from `By`
  - `elem_id: str` - element ID value based on the `elem_type`


- `navigate_to(url)` - used to navigate to the mentioned url
  - `url: str` - Target url to be navigated to


- `wait(wait_time)` - wait for mentioned time
  - `wait_time: int` - wait for the mentioned number of seconds
