import java.util.List;
import java.util.Map;
import org.openqa.selenium.support.CacheLookup;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.ui.ExpectedCondition;
import org.openqa.selenium.support.ui.Select;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class TwoPage {
    private Map<String, String> data;
    private WebDriver driver;
    private int timeout = 15;

    @FindBy(css = "a.nav-link")
    @CacheLookup
    private WebElement _1;

    @FindBy(css = "#sidebar div.sidebar-inner.affix-top section:nth-of-type(1) div.site-overview nav.site-state.motion-element div:nth-of-type(1) a")
    @CacheLookup
    private WebElement _23;

    @FindBy(css = "a[href='/404/']")
    @CacheLookup
    private WebElement _404;

    @FindBy(css = "a.brand")
    @CacheLookup
    private WebElement beautifulLove;

    @FindBy(css = "a[title='CSDN → https://me.csdn.net/nicezheng_1995']")
    @CacheLookup
    private WebElement csdn;

    @FindBy(css = "a[title='E-Mail → nicezheng@foxmail']")
    @CacheLookup
    private WebElement email;

    @FindBy(css = "a[title='GitHub → https://github.com/zhengjiani']")
    @CacheLookup
    private WebElement github;

    @FindBy(css = "a[title='MySQL存储过程及函数']")
    @CacheLookup
    private WebElement mysql1;

    @FindBy(css = "a[title='MySQL视图']")
    @CacheLookup
    private WebElement mysql2;

    @FindBy(id = "local-search-input")
    @CacheLookup
    private WebElement neverGiveUptheStrongSurvive;

    @FindBy(css = "a.theme-link")
    @CacheLookup
    private WebElement nextPisces;

    private final String pageLoadedText = "";

    private final String pageUrl = "/2019/04/15/%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F%E7%89%9B%E5%AE%A2%E7%BD%91%E7%BB%83%E4%B9%A0414/#more";

    @FindBy(css = "a[href='/atom.xml']")
    @CacheLookup
    private WebElement rss;

    public TwoPage() {
    }

    public TwoPage(WebDriver driver) {
        this();
        this.driver = driver;
    }

    public TwoPage(WebDriver driver, Map<String, String> data) {
        this(driver);
        this.data = data;
    }

    public TwoPage(WebDriver driver, Map<String, String> data, int timeout) {
        this(driver, data);
        this.timeout = timeout;
    }

    /**
     * Click on Beautiful Love Link.
     *
     * @return the TwoPage class instance.
     */
    public TwoPage clickBeautifulLoveLink() {
        beautifulLove.click();
        return this;
    }

    /**
     * Click on Csdn Link.
     *
     * @return the TwoPage class instance.
     */
    public TwoPage clickCsdnLink() {
        csdn.click();
        return this;
    }

    /**
     * Click on Email Link.
     *
     * @return the TwoPage class instance.
     */
    public TwoPage clickEmailLink() {
        email.click();
        return this;
    }

    /**
     * Click on Github Link.
     *
     * @return the TwoPage class instance.
     */
    public TwoPage clickGithubLink() {
        github.click();
        return this;
    }

    /**
     * Click on 1. Link.
     *
     * @return the TwoPage class instance.
     */
    public TwoPage clickLink1() {
        _1.click();
        return this;
    }

    /**
     * Click on 23 Link.
     *
     * @return the TwoPage class instance.
     */
    public TwoPage clickLink23() {
        _23.click();
        return this;
    }

    /**
     * Click on 404 Link.
     *
     * @return the TwoPage class instance.
     */
    public TwoPage clickLink404() {
        _404.click();
        return this;
    }

    /**
     * Click on Mysql Link.
     *
     * @return the TwoPage class instance.
     */
    public TwoPage clickMysql1Link() {
        mysql1.click();
        return this;
    }

    /**
     * Click on Mysql Link.
     *
     * @return the TwoPage class instance.
     */
    public TwoPage clickMysql2Link() {
        mysql2.click();
        return this;
    }

    /**
     * Click on Next.pisces Link.
     *
     * @return the TwoPage class instance.
     */
    public TwoPage clickNextPiscesLink() {
        nextPisces.click();
        return this;
    }

    /**
     * Click on Rss Link.
     *
     * @return the TwoPage class instance.
     */
    public TwoPage clickRssLink() {
        rss.click();
        return this;
    }

    /**
     * Fill every fields in the page.
     *
     * @return the TwoPage class instance.
     */
    public TwoPage fill() {
        setNeverGiveUptheStrongSurviveTextField();
        return this;
    }

    /**
     * Fill every fields in the page and submit it to target page.
     *
     * @return the TwoPage class instance.
     */
    public TwoPage fillAndSubmit() {
        fill();
        return submit();
    }

    /**
     * Set default value to Never Give Upthe Strong Survive Text field.
     *
     * @return the TwoPage class instance.
     */
    public TwoPage setNeverGiveUptheStrongSurviveTextField() {
        return setNeverGiveUptheStrongSurviveTextField(data.get("NEVER_GIVE_UPTHE_STRONG_SURVIVE"));
    }

    /**
     * Set value to Never Give Upthe Strong Survive Text field.
     *
     * @return the TwoPage class instance.
     */
    public TwoPage setNeverGiveUptheStrongSurviveTextField(String neverGiveUptheStrongSurviveValue) {
        neverGiveUptheStrongSurvive.sendKeys(neverGiveUptheStrongSurviveValue);
        return this;
    }

    /**
     * Submit the form to target page.
     *
     * @return the TwoPage class instance.
     */
    public TwoPage submit() {
        clickButton();
        return this;
    }

    /**
     * Verify that the page loaded completely.
     *
     * @return the TwoPage class instance.
     */
    public TwoPage verifyPageLoaded() {
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
     * @return the TwoPage class instance.
     */
    public TwoPage verifyPageUrl() {
        (new WebDriverWait(driver, timeout)).until(new ExpectedCondition<Boolean>() {
            public Boolean apply(WebDriver d) {
                return d.getCurrentUrl().contains(pageUrl);
            }
        });
        return this;
    }
}
