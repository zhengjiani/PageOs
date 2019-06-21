import java.util.List;
import java.util.Map;
import org.openqa.selenium.support.CacheLookup;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.ui.ExpectedCondition;
import org.openqa.selenium.support.ui.Select;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class BlogPage {
    private Map<String, String> data;
    private WebDriver driver;
    private int timeout = 15;

    @FindBy(css = "a[href='/2019/04/20/MySQL视图/#more']")
    @CacheLookup
    private WebElement _1;

    @FindBy(css = "a[href='/2019/04/15/操作系统牛客网练习414/#more']")
    @CacheLookup
    private WebElement _2;

    @FindBy(css = "#content nav.pagination a:nth-of-type(1)")
    @CacheLookup
    private WebElement _2;

    @FindBy(css = "#sidebar div.sidebar-inner.affix-top section.site-overview-wrap.sidebar-panel.sidebar-panel-active div.site-overview nav.site-state.motion-element div:nth-of-type(1) a")
    @CacheLookup
    private WebElement _23;

    @FindBy(css = "a[href='/2019/04/07/MySQL存储过程及函数/#more']")
    @CacheLookup
    private WebElement _3;

    @FindBy(css = "a[href='/2019/04/03/《剑指offer》刷题【1】/#more']")
    @CacheLookup
    private WebElement _4;

    @FindBy(css = "a[href='/404/']")
    @CacheLookup
    private WebElement _404;

    @FindBy(css = "a[href='/2019/04/15/操作系统牛客网练习414/']")
    @CacheLookup
    private WebElement _414;

    @FindBy(css = "a[href='/2019/04/02/MySQL索引的创建/#more']")
    @CacheLookup
    private WebElement _5;

    @FindBy(css = "a[href='/page/5/']")
    @CacheLookup
    private WebElement _5;

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

    @FindBy(css = "a[href='/2019/04/20/MySQL视图/']")
    @CacheLookup
    private WebElement mysql1;

    @FindBy(css = "a[href='/2019/04/07/MySQL存储过程及函数/']")
    @CacheLookup
    private WebElement mysql2;

    @FindBy(css = "a[href='/2019/04/02/MySQL索引的创建/']")
    @CacheLookup
    private WebElement mysql3;

    @FindBy(id = "local-search-input")
    @CacheLookup
    private WebElement neverGiveUptheStrongSurvive;

    @FindBy(css = "a.theme-link")
    @CacheLookup
    private WebElement nextPisces;

    @FindBy(css = "a[href='/2019/04/03/《剑指offer》刷题【1】/']")
    @CacheLookup
    private WebElement offer1;

    private final String pageLoadedText = "";

    private final String pageUrl = "/";

    @FindBy(css = "a[href='/atom.xml']")
    @CacheLookup
    private WebElement rss;

    public BlogPage() {
    }

    public BlogPage(WebDriver driver) {
        this();
        this.driver = driver;
    }

    public BlogPage(WebDriver driver, Map<String, String> data) {
        this(driver);
        this.data = data;
    }

    public BlogPage(WebDriver driver, Map<String, String> data, int timeout) {
        this(driver, data);
        this.timeout = timeout;
    }

    /**
     * Click on Beautiful Love Link.
     *
     * @return the BlogPage class instance.
     */
    public BlogPage clickBeautifulLoveLink() {
        beautifulLove.click();
        return this;
    }

    /**
     * Click on Csdn Link.
     *
     * @return the BlogPage class instance.
     */
    public BlogPage clickCsdnLink() {
        csdn.click();
        return this;
    }

    /**
     * Click on Email Link.
     *
     * @return the BlogPage class instance.
     */
    public BlogPage clickEmailLink() {
        email.click();
        return this;
    }

    /**
     * Click on Github Link.
     *
     * @return the BlogPage class instance.
     */
    public BlogPage clickGithubLink() {
        github.click();
        return this;
    }

    /**
     * Click on  Link.
     *
     * @return the BlogPage class instance.
     */
    public BlogPage clickLink1() {
        _1.click();
        return this;
    }

    /**
     * Click on  Link.
     *
     * @return the BlogPage class instance.
     */
    public BlogPage clickLink2() {
        _2.click();
        return this;
    }

    /**
     * Click on 2 Link.
     *
     * @return the BlogPage class instance.
     */
    public BlogPage clickLink2() {
        _2.click();
        return this;
    }

    /**
     * Click on 23 Link.
     *
     * @return the BlogPage class instance.
     */
    public BlogPage clickLink23() {
        _23.click();
        return this;
    }

    /**
     * Click on  Link.
     *
     * @return the BlogPage class instance.
     */
    public BlogPage clickLink3() {
        _3.click();
        return this;
    }

    /**
     * Click on  Link.
     *
     * @return the BlogPage class instance.
     */
    public BlogPage clickLink4() {
        _4.click();
        return this;
    }

    /**
     * Click on 404 Link.
     *
     * @return the BlogPage class instance.
     */
    public BlogPage clickLink404() {
        _404.click();
        return this;
    }

    /**
     * Click on 414 Link.
     *
     * @return the BlogPage class instance.
     */
    public BlogPage clickLink414() {
        _414.click();
        return this;
    }

    /**
     * Click on  Link.
     *
     * @return the BlogPage class instance.
     */
    public BlogPage clickLink5() {
        _5.click();
        return this;
    }

    /**
     * Click on 5 Link.
     *
     * @return the BlogPage class instance.
     */
    public BlogPage clickLink5() {
        _5.click();
        return this;
    }

    /**
     * Click on Mysql Link.
     *
     * @return the BlogPage class instance.
     */
    public BlogPage clickMysql1Link() {
        mysql1.click();
        return this;
    }

    /**
     * Click on Mysql Link.
     *
     * @return the BlogPage class instance.
     */
    public BlogPage clickMysql2Link() {
        mysql2.click();
        return this;
    }

    /**
     * Click on Mysql Link.
     *
     * @return the BlogPage class instance.
     */
    public BlogPage clickMysql3Link() {
        mysql3.click();
        return this;
    }

    /**
     * Click on Next.pisces Link.
     *
     * @return the BlogPage class instance.
     */
    public BlogPage clickNextPiscesLink() {
        nextPisces.click();
        return this;
    }

    /**
     * Click on Offer1 Link.
     *
     * @return the BlogPage class instance.
     */
    public BlogPage clickOffer1Link() {
        offer1.click();
        return this;
    }

    /**
     * Click on Rss Link.
     *
     * @return the BlogPage class instance.
     */
    public BlogPage clickRssLink() {
        rss.click();
        return this;
    }

    /**
     * Fill every fields in the page.
     *
     * @return the BlogPage class instance.
     */
    public BlogPage fill() {
        setNeverGiveUptheStrongSurviveTextField();
        return this;
    }

    /**
     * Fill every fields in the page and submit it to target page.
     *
     * @return the BlogPage class instance.
     */
    public BlogPage fillAndSubmit() {
        fill();
        return submit();
    }

    /**
     * Set default value to Never Give Upthe Strong Survive Text field.
     *
     * @return the BlogPage class instance.
     */
    public BlogPage setNeverGiveUptheStrongSurviveTextField() {
        return setNeverGiveUptheStrongSurviveTextField(data.get("NEVER_GIVE_UPTHE_STRONG_SURVIVE"));
    }

    /**
     * Set value to Never Give Upthe Strong Survive Text field.
     *
     * @return the BlogPage class instance.
     */
    public BlogPage setNeverGiveUptheStrongSurviveTextField(String neverGiveUptheStrongSurviveValue) {
        neverGiveUptheStrongSurvive.sendKeys(neverGiveUptheStrongSurviveValue);
        return this;
    }

    /**
     * Submit the form to target page.
     *
     * @return the BlogPage class instance.
     */
    public BlogPage submit() {
        clickButton();
        return this;
    }

    /**
     * Verify that the page loaded completely.
     *
     * @return the BlogPage class instance.
     */
    public BlogPage verifyPageLoaded() {
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
     * @return the BlogPage class instance.
     */
    public BlogPage verifyPageUrl() {
        (new WebDriverWait(driver, timeout)).until(new ExpectedCondition<Boolean>() {
            public Boolean apply(WebDriver d) {
                return d.getCurrentUrl().contains(pageUrl);
            }
        });
        return this;
    }
}
