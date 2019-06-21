import java.util.List;
import java.util.Map;
import org.openqa.selenium.support.CacheLookup;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.ui.ExpectedCondition;
import org.openqa.selenium.support.ui.Select;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class OnePage {
    private Map<String, String> data;
    private WebDriver driver;
    private int timeout = 15;

    @FindBy(css = "#sidebar div.sidebar-inner.affix-top section:nth-of-type(2) div.post-toc div.post-toc-content ol.nav li.nav-item.nav-level-2.active.active-current ol.nav-child li:nth-of-type(1) a.nav-link")
    @CacheLookup
    private WebElement _11;

    @FindBy(css = "#sidebar div.sidebar-inner.affix-top section:nth-of-type(2) div.post-toc div.post-toc-content ol.nav li.nav-item.nav-level-2.active.active-current ol.nav-child li:nth-of-type(10) a.nav-link")
    @CacheLookup
    private WebElement _110;

    @FindBy(css = "#sidebar div.sidebar-inner.affix-top section:nth-of-type(2) div.post-toc div.post-toc-content ol.nav li.nav-item.nav-level-2.active.active-current ol.nav-child li:nth-of-type(2) a.nav-link")
    @CacheLookup
    private WebElement _12;

    @FindBy(css = "#sidebar div.sidebar-inner.affix-top section:nth-of-type(2) div.post-toc div.post-toc-content ol.nav li.nav-item.nav-level-2.active.active-current ol.nav-child li:nth-of-type(3) a.nav-link")
    @CacheLookup
    private WebElement _13;

    @FindBy(css = "#sidebar div.sidebar-inner.affix-top section:nth-of-type(2) div.post-toc div.post-toc-content ol.nav li.nav-item.nav-level-2.active.active-current ol.nav-child li:nth-of-type(4) a.nav-link")
    @CacheLookup
    private WebElement _14;

    @FindBy(css = "#sidebar div.sidebar-inner.affix-top section:nth-of-type(2) div.post-toc div.post-toc-content ol.nav li.nav-item.nav-level-2.active.active-current ol.nav-child li:nth-of-type(5) a.nav-link")
    @CacheLookup
    private WebElement _15;

    @FindBy(css = "#sidebar div.sidebar-inner.affix-top section:nth-of-type(2) div.post-toc div.post-toc-content ol.nav li.nav-item.nav-level-2.active.active-current ol.nav-child li:nth-of-type(7) a.nav-link")
    @CacheLookup
    private WebElement _17;

    @FindBy(css = "#sidebar div.sidebar-inner.affix-top section:nth-of-type(2) div.post-toc div.post-toc-content ol.nav li.nav-item.nav-level-2.active.active-current ol.nav-child li:nth-of-type(8) a.nav-link")
    @CacheLookup
    private WebElement _18;

    @FindBy(css = "#sidebar div.sidebar-inner.affix-top section:nth-of-type(2) div.post-toc div.post-toc-content ol.nav li.nav-item.nav-level-2.active.active-current ol.nav-child li:nth-of-type(9) a.nav-link")
    @CacheLookup
    private WebElement _19;

    @FindBy(css = "#sidebar div.sidebar-inner.affix-top section:nth-of-type(1) div.site-overview nav.site-state.motion-element div:nth-of-type(1) a")
    @CacheLookup
    private WebElement _23;

    @FindBy(css = "a[href='/404/']")
    @CacheLookup
    private WebElement _404;

    @FindBy(css = "a[title='操作系统牛客网练习414']")
    @CacheLookup
    private WebElement _414;

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

    @FindBy(css = "a[href='/tags/MySQL/']")
    @CacheLookup
    private WebElement mysql;

    @FindBy(css = "#sidebar div.sidebar-inner.affix-top section:nth-of-type(2) div.post-toc div.post-toc-content ol.nav li.nav-item.nav-level-2.active.active-current a.nav-link")
    @CacheLookup
    private WebElement mysql1;

    @FindBy(id = "local-search-input")
    @CacheLookup
    private WebElement neverGiveUptheStrongSurvive;

    @FindBy(css = "a.theme-link")
    @CacheLookup
    private WebElement nextPisces;

    private final String pageLoadedText = "";

    private final String pageUrl = "/2019/04/20/MySQL%E8%A7%86%E5%9B%BE/#more";

    @FindBy(css = "a[href='/atom.xml']")
    @CacheLookup
    private WebElement rss;

    @FindBy(css = "#sidebar div.sidebar-inner.affix-top section:nth-of-type(2) div.post-toc div.post-toc-content ol.nav li.nav-item.nav-level-2.active.active-current ol.nav-child li:nth-of-type(6) a.nav-link")
    @CacheLookup
    private WebElement views16;

    public OnePage() {
    }

    public OnePage(WebDriver driver) {
        this();
        this.driver = driver;
    }

    public OnePage(WebDriver driver, Map<String, String> data) {
        this(driver);
        this.data = data;
    }

    public OnePage(WebDriver driver, Map<String, String> data, int timeout) {
        this(driver, data);
        this.timeout = timeout;
    }

    /**
     * Click on Beautiful Love Link.
     *
     * @return the OnePage class instance.
     */
    public OnePage clickBeautifulLoveLink() {
        beautifulLove.click();
        return this;
    }

    /**
     * Click on Csdn Link.
     *
     * @return the OnePage class instance.
     */
    public OnePage clickCsdnLink() {
        csdn.click();
        return this;
    }

    /**
     * Click on Email Link.
     *
     * @return the OnePage class instance.
     */
    public OnePage clickEmailLink() {
        email.click();
        return this;
    }

    /**
     * Click on Github Link.
     *
     * @return the OnePage class instance.
     */
    public OnePage clickGithubLink() {
        github.click();
        return this;
    }

    /**
     * Click on 1.1. Link.
     *
     * @return the OnePage class instance.
     */
    public OnePage clickLink11() {
        _11.click();
        return this;
    }

    /**
     * Click on 1.10. Link.
     *
     * @return the OnePage class instance.
     */
    public OnePage clickLink110() {
        _110.click();
        return this;
    }

    /**
     * Click on 1.2. Link.
     *
     * @return the OnePage class instance.
     */
    public OnePage clickLink12() {
        _12.click();
        return this;
    }

    /**
     * Click on 1.3. Link.
     *
     * @return the OnePage class instance.
     */
    public OnePage clickLink13() {
        _13.click();
        return this;
    }

    /**
     * Click on 1.4. Link.
     *
     * @return the OnePage class instance.
     */
    public OnePage clickLink14() {
        _14.click();
        return this;
    }

    /**
     * Click on 1.5. Link.
     *
     * @return the OnePage class instance.
     */
    public OnePage clickLink15() {
        _15.click();
        return this;
    }

    /**
     * Click on 1.7. Link.
     *
     * @return the OnePage class instance.
     */
    public OnePage clickLink17() {
        _17.click();
        return this;
    }

    /**
     * Click on 1.8. Link.
     *
     * @return the OnePage class instance.
     */
    public OnePage clickLink18() {
        _18.click();
        return this;
    }

    /**
     * Click on 1.9. Link.
     *
     * @return the OnePage class instance.
     */
    public OnePage clickLink19() {
        _19.click();
        return this;
    }

    /**
     * Click on 23 Link.
     *
     * @return the OnePage class instance.
     */
    public OnePage clickLink23() {
        _23.click();
        return this;
    }

    /**
     * Click on 404 Link.
     *
     * @return the OnePage class instance.
     */
    public OnePage clickLink404() {
        _404.click();
        return this;
    }

    /**
     * Click on 414 Link.
     *
     * @return the OnePage class instance.
     */
    public OnePage clickLink414() {
        _414.click();
        return this;
    }

    /**
     * Click on Mysql Link.
     *
     * @return the OnePage class instance.
     */
    public OnePage clickMysqlLink() {
        mysql.click();
        return this;
    }

    /**
     * Click on 1. Mysql Link.
     *
     * @return the OnePage class instance.
     */
    public OnePage clickMysqlLink1() {
        mysql1.click();
        return this;
    }

    /**
     * Click on Next.pisces Link.
     *
     * @return the OnePage class instance.
     */
    public OnePage clickNextPiscesLink() {
        nextPisces.click();
        return this;
    }

    /**
     * Click on Rss Link.
     *
     * @return the OnePage class instance.
     */
    public OnePage clickRssLink() {
        rss.click();
        return this;
    }

    /**
     * Click on 1.6. Views Link.
     *
     * @return the OnePage class instance.
     */
    public OnePage clickViewsLink16() {
        views16.click();
        return this;
    }

    /**
     * Fill every fields in the page.
     *
     * @return the OnePage class instance.
     */
    public OnePage fill() {
        setNeverGiveUptheStrongSurviveTextField();
        return this;
    }

    /**
     * Fill every fields in the page and submit it to target page.
     *
     * @return the OnePage class instance.
     */
    public OnePage fillAndSubmit() {
        fill();
        return submit();
    }

    /**
     * Set default value to Never Give Upthe Strong Survive Text field.
     *
     * @return the OnePage class instance.
     */
    public OnePage setNeverGiveUptheStrongSurviveTextField() {
        return setNeverGiveUptheStrongSurviveTextField(data.get("NEVER_GIVE_UPTHE_STRONG_SURVIVE"));
    }

    /**
     * Set value to Never Give Upthe Strong Survive Text field.
     *
     * @return the OnePage class instance.
     */
    public OnePage setNeverGiveUptheStrongSurviveTextField(String neverGiveUptheStrongSurviveValue) {
        neverGiveUptheStrongSurvive.sendKeys(neverGiveUptheStrongSurviveValue);
        return this;
    }

    /**
     * Submit the form to target page.
     *
     * @return the OnePage class instance.
     */
    public OnePage submit() {
        clickButton();
        return this;
    }

    /**
     * Verify that the page loaded completely.
     *
     * @return the OnePage class instance.
     */
    public OnePage verifyPageLoaded() {
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
     * @return the OnePage class instance.
     */
    public OnePage verifyPageUrl() {
        (new WebDriverWait(driver, timeout)).until(new ExpectedCondition<Boolean>() {
            public Boolean apply(WebDriver d) {
                return d.getCurrentUrl().contains(pageUrl);
            }
        });
        return this;
    }
}
