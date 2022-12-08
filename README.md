# Web Automation Framework

This is a project designed to minimize the setup and config of selenium and actions performed on elements

To use this library, create a snippet like below and populate the actions in the `run` method (remove the `pass` keyword)

```python
from web_automation.framework import Framework, Browser

class CustomClass(Framework):
    def run(self):
        pass

CustomClass(
    browser=Browser.CHROME,  # Accepted browsers [CHROME|EDGE|FIREFOX]
    wait=10,  # Implicit wait for an element to be present in the document, optional, default value is 30 secs
    headless=False,  # Open the browser in headless mode, optional, default value is False
    download_path=''  # Custom download path, optional, default value is system download folder
)
```
