import java.util.List;
import java.util.Map;
import org.openqa.selenium.support.CacheLookup;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.ui.ExpectedCondition;
import org.openqa.selenium.support.ui.Select;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class findpage {
    private Map<String, String> data;
    private WebDriver driver;
    private int timeout = 30;

    @FindBy(css = "a.btn.btn-default")
    @CacheLookup
    private WebElement addOwner;

    @FindBy(css = "a[title='trigger a RuntimeException to see how it is handled']")
    @CacheLookup
    private WebElement error;

    @FindBy(css = "button.btn.btn-default")
    @CacheLookup
    private WebElement findOwner;

    @FindBy(css = "a[title='find owners']")
    @CacheLookup
    private WebElement findOwners;

    @FindBy(css = "a[title='home page']")
    @CacheLookup
    private WebElement home;

    @FindBy(id = "lastName")
    @CacheLookup
    private WebElement lastName;

    private final String pageLoadedText = "";

    private final String pageUrl = "/owners/find";

    @FindBy(css = "button.navbar-toggle")
    @CacheLookup
    private WebElement toggleNavigation;

    @FindBy(css = "a[title='veterinarians']")
    @CacheLookup
    private WebElement veterinarians;

    public findpage() {
    }

    public findpage(WebDriver driver) {
        this();
        this.driver = driver;
    }

    public findpage(WebDriver driver, Map<String, String> data) {
        this(driver);
        this.data = data;
    }

    public findpage(WebDriver driver, Map<String, String> data, int timeout) {
        this(driver, data);
        this.timeout = timeout;
    }

    /**
     * Click on Add Owner Link.
     *
     * @return the findpage class instance.
     */
    public findpage clickAddOwnerLink() {
        addOwner.click();
        return this;
    }

    /**
     * Click on Error Link.
     *
     * @return the findpage class instance.
     */
    public findpage clickErrorLink() {
        error.click();
        return this;
    }

    /**
     * Click on Find Owner Button.
     *
     * @return the findpage class instance.
     */
    public findpage clickFindOwnerButton() {
        findOwner.click();
        return this;
    }

    /**
     * Click on Find Owners Link.
     *
     * @return the findpage class instance.
     */
    public findpage clickFindOwnersLink() {
        findOwners.click();
        return this;
    }

    /**
     * Click on Home Link.
     *
     * @return the findpage class instance.
     */
    public findpage clickHomeLink() {
        home.click();
        return this;
    }

    /**
     * Click on Toggle Navigation Button.
     *
     * @return the findpage class instance.
     */
    public findpage clickToggleNavigationButton() {
        toggleNavigation.click();
        return this;
    }

    /**
     * Click on Veterinarians Link.
     *
     * @return the findpage class instance.
     */
    public findpage clickVeterinariansLink() {
        veterinarians.click();
        return this;
    }

    /**
     * Fill every fields in the page.
     *
     * @return the findpage class instance.
     */
    public findpage fill() {
        setLastNameTextField();
        return this;
    }

    /**
     * Fill every fields in the page and submit it to target page.
     *
     * @return the findpage class instance.
     */
    public findpage fillAndSubmit() {
        fill();
        return submit();
    }

    /**
     * Set default value to Last Name Text field.
     *
     * @return the findpage class instance.
     */
    public findpage setLastNameTextField() {
        return setLastNameTextField(data.get("LAST_NAME"));
    }

    /**
     * Set value to Last Name Text field.
     *
     * @return the findpage class instance.
     */
    public findpage setLastNameTextField(String lastNameValue) {
        lastName.sendKeys(lastNameValue);
        return this;
    }

    /**
     * Submit the form to target page.
     *
     * @return the findpage class instance.
     */
    public findpage submit() {
        clickFindOwnerButton();
        return this;
    }

    /**
     * Verify that the page loaded completely.
     *
     * @return the findpage class instance.
     */
    public findpage verifyPageLoaded() {
        (new WebDriverWait(driver, timeout)).until(new ExpectedCondition<Boolean>() {
            public Boolean apply(WebDriver d) {
                return d.getPageSource().contains(pageLoadedText);
            }
        });
        return this;
    }

    /**
     * Verify that current page URL matches the expected URL.
     *
     * @return the findpage class instance.
     */
    public findpage verifyPageUrl() {
        (new WebDriverWait(driver, timeout)).until(new ExpectedCondition<Boolean>() {
            public Boolean apply(WebDriver d) {
                return d.getCurrentUrl().contains(pageUrl);
            }
        });
        return this;
    }
}
