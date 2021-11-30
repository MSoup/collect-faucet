# Random Findings / References / Notes to Self

# Selenium is not a test framework

![Test Framework](https://www.selenium.dev/images/documentation/webdriver/test_framework.png)

It allows you to automate actions on the browser through a webdriver. The webdriver communicates with the browser via a driver, and the browser sends responses back via the same driver. **Test frameworks are to be implemented in a way that uses selenium.**

# Focusing

WebDriver does not make the distinction between windows and tabs. If your site opens a new tab or window, Selenium will let you work with it using a window handle. Each window has a unique identifier which remains persistent in a single session. You can get the window handle of the current window by using:

```python
driver.current_window_handle
```

# Testing

Types of tests

1. Acceptance Testing

   Does a feature meet the customer expectations and requirements? Requires customer feedback. This test answers the question: "are we building the **right** product?" 

   We can simulate user expected behavior via Selenium, via Record/playback or through supported languages.

   Acceptance testing is a subtype of functional testing

2. Functional Testing

   Determines if a feature functions properly without issues

   Checks system at different levels to ensure all scenarios are covered. This test answers the question: "are we building the product **right?**"

   Tests include tests that work without errors like 404s and exceptions, and has the correct redirections.

   Via Selenium we simulate expected returns. Record/playback or through supported languages.

3. Performance Testing

   In performance testing, we should test

   a. Load testing: how well the app works under different defined loads (x users connected at once)

   b. Stress testing: how well it works under stress (above max supported load)

   Performance tests are done by executing some Selenium written tests simulating different users hitting functions and retrieving meaningful measurements. Use tools like JMeter.

   We should measure throughput, latency, data loss, individual component loading times.

4. Regression Testing

   This test is done after a change, fix, or feature addition

   Makes sure no existing functionality was broken. 

5. Test Driven Development (TDD)

   Each dev cycle starts by creating a set of unit tests that the feature should eventually pass (they should fail their first time executed)

   After this, make the tests pass. 

6. Behavior Driven Development (BDD)

   BDD is based on TDD. Each cycle starts by creating some specs (which should fail). Then create the failing unit tests (that will fail too), then do the development. Most tools use Gherkin as the language. Tools to write the specs and match with code functions are **Cucumber** or **SpecFlow**

   A set of tools are built on top of Selenium to make this process even faster by directly transforming the BDD specifications into executable code. Some of these are ***JBehave, Capybara and Robot Framework\***.

# Page Object Models

Page Object Models is a design pattern. It's an object oriented class that's used as an interface for application under test (AUT). The tests use the methods of this class whenever they need to access the UI. 

The benefit is if the UI changes for the page, the tests themselves dont need to change. Only the code within the page object needs to change. All changes to support that new UI are located in one place.

Main advantages:

- Separation between test code and page specific code such as locators and layout
- Single repo for services/operations offered by the page rather than having the services scattered throughout the tests

Example

```java
/***
 * Tests login feature
 */
public class Login {

  public void testLogin() {
    // fill login data on sign-in page
    driver.findElement(By.name("user_name")).sendKeys("testUser");
    driver.findElement(By.name("password")).sendKeys("my supersecret password");
    driver.findElement(By.name("sign-in")).click();

    // verify h1 tag is "Hello userName" after login
    driver.findElement(By.tagName("h1")).isDisplayed();
    assertThat(driver.findElement(By.tagName("h1")).getText(), is("Hello userName"));
  }
}
```

Looks ok, BUT

There are two problems with this approach:

- no separation between the test method and the AUT's locators (IDs in this ex); they're intertwined in a single method. If the AUT's UI changes its identifiers, layouts, how a login is input and processed, the whole test needs to change right?
- The ID locators would spread in multiple tests, in all tests that had to use this login page.

Here's how we can apply page object techniques:

Page Object for a sign in page

```java
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

/**
 * Page Object encapsulates the Sign-in page.
 */
public class SignInPage {
  protected WebDriver driver;

  // <input name="user_name" type="text" value="">
  private By usernameBy = By.name("user_name");
  // <input name="password" type="password" value="">
  private By passwordBy = By.name("password");
  // <input name="sign_in" type="submit" value="SignIn">
  private By signinBy = By.name("sign_in");

  public SignInPage(WebDriver driver){
    this.driver = driver;
  }

  /**
    * Login as valid user
    *
    * @param userName
    * @param password
    * @return HomePage object
    */
  public HomePage loginValidUser(String userName, String password) {
    driver.findElement(usernameBy).sendKeys(userName);
    driver.findElement(passwordBy).sendKeys(password);
    driver.findElement(signinBy).click();
    return new HomePage(driver);
  }
}

```

Page object for a home page 

```java
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

/**
 * Page Object encapsulates the Home Page
 */
public class HomePage {
  protected WebDriver driver;

  // <h1>Hello userName</h1>
  private By messageBy = By.tagName("h1");

  public HomePage(WebDriver driver){
    this.driver = driver;
    if (!driver.getTitle().equals("Home Page of logged in user")) {
      throw new IllegalStateException("This is not Home Page of logged in user," +
            " current page is: " + driver.getCurrentUrl());
    }
  }

  /**
    * Get message (h1 tag)
    *
    * @return String message text
    */
  public String getMessageText() {
    return driver.findElement(messageBy).getText();
  }

  public HomePage manageProfile() {
    // Page encapsulation to manage profile functionality
    return new HomePage(driver);
  }
  /* More methods offering the services represented by Home Page
  of Logged User. These methods in turn might return more Page Objects
  for example click on Compose mail button could return ComposeMail class object */
}

```



And now, the login test: uses the two page objects

```java
/***
 * Tests login feature
 */
public class TestLogin {

  @Test
  public void testLogin() {
    SignInPage signInPage = new SignInPage(driver);
    HomePage homePage = signInPage.loginValidUser("userName", "password");
    assertThat(homePage.getMessageText(), is("Hello userName"));
  }

}
```



Key takeaways:

Page objects themselves should never make verifications or assertions. This is part of your test and should always be within the test’s code, never in an page object. The page object will contain the representation of the page, and the services the page provides via methods but no code related to what is being tested should be within the page object.

There is one, single, verification which can, and should, be within the page object and that is to verify that the page, and possibly critical elements on the page, were loaded correctly.





## Diving Deeper Into Elements

As seen in the example, locating elements in WebDriver is done on the WebDriver instance object. The findElement(By) method returns another fundamental object type, the WebElement.

WebDriver represents the browser
WebElement represents a particular DOM node (a control, e.g. a link or input field, etc.)

Once you have a reference to a web element that’s been “found”, you can narrow the scope of your search by using the same call on that object instance:


```
cheese = driver.find_element(By.ID, "cheese")
cheddar = cheese.find_elements_by_id("cheddar")
```

In general, if HTML IDs are available, unique, and consistently predictable, they are the preferred method for locating an element on a page. They tend to work very quickly, and forego much processing that comes with complicated DOM traversals.

If unique IDs are unavailable, a well-written CSS selector is the preferred method of locating an element. XPath works as well as CSS selectors, but the syntax is complicated and frequently difficult to debug. Though XPath selectors are very flexible, they are typically not performance tested by browser vendors and tend to be quite slow.

## Explicit Waits

Dealing with Async operations

The conditions available in the different language bindings vary, but this is a non-exhaustive list of a few:

alert is present
element exists
element is visible
title contains
title is
element staleness
visible text

See https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html?highlight=expected

Example
```
from selenium.webdriver.support.ui import WebDriverWait

driver.navigate("file:///race_condition.html")
el = WebDriverWait(driver).until(lambda d: d.find_element_by_tag_name("p"))
assert el.text == "Hello from JavaScript!"
```