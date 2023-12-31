onst axios = require('axios');
const fs = require('fs');
const path = require('path');
const markdownify = require('markdownify');
const { JSDOM } = require('jsdom');

// Fetch articles
async function fetchArticles(language) {
  let page = 1;
  let articles = [];
  
  while (true) {
    const response = await axios.get(`https://support.metamask.io/api/v2/help_center/${language}/articles.json?page=${page}`);
    const data = response.data;
    
    if (!data.articles || data.articles.length === 0) {
      break;
    }
    
    articles.push(...data.articles);
    page++;
  }
  
  return articles;
}

// Convert HTML to Markdown
function htmlToMarkdown(html) {
  return markdownify(html); 
}

// Update image links 
function updateImageLinks(html, imageFiles, imageDir) {
  const dom = new JSDOM(html);
  const { document } = dom.window;
  
  document.querySelectorAll('img').forEach(img => {
    const src = img.getAttribute('src');
    const imageFilename = path.basename(src);
    
    const newSrc = imageFiles.find(f => path.basename(f) === imageFilename);
    if (newSrc) {
      img.setAttribute('src', path.relative(imageDir, newSrc));
    }
  });
  
  return dom.serialize();
}

// Format tabs
function formatTabs(html) {
  const dom = new JSDOM(html);
  const { document } = dom.window;

  document.querySelectorAll('.tabs').forEach(tabs => {
    const tabLabels = tabs.querySelectorAll('.tabs-link');
    const tabContents = tabs.querySelectorAll('.tab');
    
    const tabsComponent = `
      <Tabs>
        ${tabLabels.map((label, i) => {
          return `
            <TabItem value="${label.textContent}" label="${label.textContent}">
              ${tabContents[i].innerHTML}
            </TabItem>  
          `;
        }).join('\n')}
      </Tabs>
    `;
    
    tabs.replaceWith(dom.window.document.createRange().createContextualFragment(tabsComponent));
  });

  return dom.serialize();
}

// Format callouts
function formatCallouts(html) {
  const dom = new JSDOM(html);
  const { document } = dom.window;

  document.querySelectorAll('.callout').forEach(callout => {
    let type;
    if (callout.classList.contains('callout--info')) {
      type = 'info';
    } else if (callout.classList.contains('callout--transparent')) {
      type = 'note'; 
    } else if (callout.classList.contains('callout--success')) {
      type = 'tip';
    } else if (callout.classList.contains('callout--warning')) {
      type = 'warning';
    } else if (callout.classList.contains('callout--danger')) {
      type = 'danger';
    } else {
      type = 'note';
    }

    const title = callout.querySelector('.callout__title')?.textContent ?? '';
    const content = callout.querySelector('p')?.innerHTML ?? '';

    const calloutComponent = `
      :::${type}[${title}]
      
      ${content}
      
      :::
    `;

    callout.replaceWith(dom.window.document.createRange().createContextualFragment(calloutComponent));
  });

  return dom.serialize();
}

// Main function
async function convertArticles(languages, imageDir) {
  const imageFiles = getImageFiles(imageDir);

  for (const language of languages) {
    const articles = await fetchArticles(language);

    articles.forEach(article => {
      const { title, body, section_id } = article;
      const filename = sanitizeFilename(title);
      const filePath = getFilePath(filename, language, section_id);

      let content = body;
      content = updateImageLinks(content, imageFiles, imageDir);
      content = formatTabs(content);
      content = formatCallouts(content);
      content = htmlToMarkdown(content);

      const frontMatter = `---\ntitle: '${title}'\n---\n\n`;

      fs.writeFileSync(filePath, frontMatter + content);
    });
  }
}

// Helper functions
function sanitizeFilename(filename) {
  // ...
}

function getFilePath(filename, language, sectionId) {
  // ... 
}

function getImageFiles(dir) {
  // ...
}

const languages = [/*...*/]; 
const imageDir = './images';

convertArticles(languages, imageDir);