// const path = require("path");
const scraperObject = {
  url: "https://www.ncei.noaa.gov/access/search/data-search/local-climatological-data?pageNum=1&startDate=2010-01-01T00:00:00&endDate=2024-01-01T23:59:59&dataTypes=HTDD",
  async scraper(browser) {
    try {
      const states = [
        "Alabama",
        "Alaska",
        "Arizona",
        "Arkansas",
        "California",
        "Colorado",
        "Connecticut",
        "Delaware",
        "Florida",
        "Georgia",
        "Hawaii",
        "Idaho",
        "Illinois",
        "Indiana",
        "Iowa",
        "Kansas",
        "Kentucky",
        "Louisiana",
        "Maine",
        "Maryland",
        "Massachusetts",
        "Michigan",
        "Minnesota",
        "Mississippi",
        "Missouri",
        "Montana",
        "Nebraska",
        "Nevada",
        "New Hampshire",
        "New Jersey",
        "New Mexico",
        "New York",
        "North Carolina",
        "North Dakota",
        "Ohio",
        "Oklahoma",
        "Oregon",
        "Pennsylvania",
        "Rhode Island",
        "South Carolina",
        "South Dakota",
        "Tennessee",
        "Texas",
        "Utah",
        "Vermont",
        "Virginia",
        "Washington",
        "West Virginia",
        "Wisconsin",
        "Wyoming",
      ];
      function delay(time) {
        return new Promise(function (resolve) {
          setTimeout(resolve, time);
        });
      }

      let page = await browser.newPage();
      console.log(`Navigating to ${this.url}...`);
      await page.goto(this.url);

      for (const state of states) {
        console.log("state:", state);
        let finished = false;
        await page.waitForSelector(".fa-download");
        await delay(1000);

        await page.type("#whereInput", state);
        await delay(1000);
        await page.keyboard.press("ArrowDown");
        await delay(500);
        await page.keyboard.press("Enter");

        await delay(2000);
        while (!finished) {
          try {
            const nextButtonDisabled = await page.$eval(
              ".disabled",
              (a) => a.textContent === "»"
            );
            if (nextButtonDisabled) {
              finished = true;
            }
          } catch (err) {}
          await page.$$eval(".fa-download", (buttons) => {
            buttons.forEach(async (button) => {
              await button.click();
            });
          });

          await delay(4000);

          await page.$$eval(".page-link", (buttons) => {
            buttons.forEach(async (button) => {
              if (button.textContent === "»") {
                await button.click();
              }
            });
          });
          await delay(4000);
        }
      }

      console.log("Job Finished");
    } catch (err) {
      console.log("error:", err);
    }
  },
};

module.exports = scraperObject;
