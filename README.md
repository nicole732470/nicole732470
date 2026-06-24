<div align="center">

<img src="https://readme-typing-svg.demolab.com/?lines=oh+hey+~+%F0%9F%91%8B;building+tools+for+job+search+%26+shopping;projects+below+%E2%86%93&font=Fira+Code&size=22&duration=2600&pause=1200&color=7C9CFF&center=true&width=400" alt=""/>

<br/>

<pre style="font-size:15px;line-height:1.7;text-align:center;margin:0;color:#57606a;">
  ✧ ˚  n i c o l e   l i  ˚ ✧

       (\__/)
       (•ㅅ•)  engineering × product
      /  づ   chicago · northwestern · tencent · open to work
</pre>

</div>

<br/>

## projects

<br/>

<div style="border:1px solid #d8dee4;border-radius:14px;background:#ffffff;padding:20px;margin-bottom:20px;max-width:100%;box-sizing:border-box;">

<b style="font-size:17px;color:#24292f;display:block;margin-bottom:10px;">🛒 <a href="https://github.com/nicole732470/smartshoppinglist" style="color:#24292f;text-decoration:none;">PriceTracker</a></b>

<a href="https://github.com/nicole732470/smartshoppinglist">
<img src="./assets/project-pricetracker.png" width="100%" alt="PriceTracker" style="border-radius:10px;border:1px solid #d0d7de;margin-bottom:14px;display:block;max-width:100%;height:auto;"/>
</a>

<span style="font-size:14px;color:#24292f;line-height:1.6;display:block;margin-bottom:8px;">
A full-stack price watching app — paste a product URL, track history across stores, and get notified when prices drop.
</span>

<span style="font-size:13px;color:#57606a;line-height:1.65;display:block;margin-bottom:10px;">
· Paste a retailer link → auto-fetch title, image, and current price<br/>
· Dashboard with price history charts and target-price alerts<br/>
· 16 supported retailers (Amazon, Best Buy, Walmart, Lululemon, Apple, and more)<br/>
· Account settings, email notifications, Cucumber + RSpec test suite
</span>

<span style="font-size:12px;color:#57606a;display:block;margin-bottom:10px;">
<code>Ruby on Rails</code> · <code>PostgreSQL</code> · <code>Heroku</code> · <code>Active Storage</code>
</span>

<pre style="font-size:11px;line-height:1.5;color:#57606a;background:#f6f8fa;border:1px solid #d0d7de;border-radius:8px;padding:12px;margin:0;white-space:pre-wrap;word-wrap:break-word;">
URL → fetch metadata → price history → dashboard + alerts
</pre>

<span style="font-size:13px;display:block;margin-top:12px;">
<a href="https://github.com/nicole732470/smartshoppinglist" style="color:#0969da;">GitHub</a>
&nbsp;·&nbsp;
<a href="https://smart-shoppinglist-6ae31171e85c.herokuapp.com/" style="color:#0969da;">live app</a>
</span>

</div>

<div style="border:1px solid #d8dee4;border-radius:14px;background:#ffffff;padding:20px;margin-bottom:20px;max-width:100%;box-sizing:border-box;">

<b style="font-size:17px;color:#24292f;display:block;margin-bottom:10px;">🔍 <a href="https://github.com/nicole732470/joblens" style="color:#24292f;text-decoration:none;">JobLens</a></b>

<a href="https://job-lens-main.lovable.app">
<img src="./assets/project-joblens.png" width="100%" alt="JobLens" style="border-radius:10px;border:1px solid #d0d7de;margin-bottom:14px;display:block;max-width:100%;height:auto;"/>
</a>

<span style="font-size:14px;color:#24292f;line-height:1.6;display:block;margin-bottom:8px;">
Visa-aware job-fit assistant — paste a posting or use the Chrome extension on LinkedIn and get an evidence-backed Apply / Consider / Skip report.
</span>

<span style="font-size:13px;color:#57606a;line-height:1.65;display:block;margin-bottom:10px;">
· DOL H-1B / LCA employer history lookup on every company<br/>
· Role, Resume, Location, and Company fit scoring with cited evidence<br/>
· Preference and dealbreaker checks against your profile<br/>
· Same API + report for web app and LinkedIn Chrome extension<br/>
· FastAPI + LangGraph pipeline with deterministic guardrails
</span>

<span style="font-size:12px;color:#57606a;display:block;margin-bottom:10px;">
<code>FastAPI</code> · <code>LangGraph</code> · <code>PostgreSQL</code> · <code>AWS RDS</code> · <code>Chrome MV3</code> · <code>React</code>
</span>

<pre style="font-size:11px;line-height:1.5;color:#57606a;background:#f6f8fa;border:1px solid #d0d7de;border-radius:8px;padding:12px;margin:0;white-space:pre-wrap;word-wrap:break-word;">
JD → LCA lookup → parallel fit scores → guardrails → verdict
</pre>

<span style="font-size:13px;display:block;margin-top:12px;">
<a href="https://github.com/nicole732470/joblens" style="color:#0969da;">GitHub</a>
&nbsp;·&nbsp;
<a href="https://job-lens-main.lovable.app" style="color:#0969da;">live app</a>
</span>

</div>

<div style="border:1px solid #d8dee4;border-radius:14px;background:#ffffff;padding:20px;margin-bottom:20px;max-width:100%;box-sizing:border-box;">

<b style="font-size:17px;color:#24292f;display:block;margin-bottom:10px;">🚀 <a href="https://github.com/nicole732470/jobpush" style="color:#24292f;text-decoration:none;">JobPush</a></b>

<a href="https://github.com/nicole732470/jobpush">
<img src="./assets/project-jobpush.png" width="100%" alt="JobPush" style="border-radius:10px;border:1px solid #d0d7de;margin-bottom:14px;display:block;max-width:100%;height:auto;"/>
</a>

<span style="font-size:14px;color:#24292f;line-height:1.6;display:block;margin-bottom:8px;">
Prioritized company career-site discovery and official job-posting monitoring — the crawl layer behind the JobLens ecosystem.
</span>

<span style="font-size:13px;color:#57606a;line-height:1.65;display:block;margin-bottom:10px;">
· Explainable priority scoring from DOL LCA data (target SOC, salary, Chicago metro, and more)<br/>
· <code>company_targets</code> audit table refreshed from shared company + LCA sources<br/>
· Career-site discovery pilots with adapter-specific crawl execution<br/>
· Shares AWS RDS with JobLens; owns the <code>jobpush</code> PostgreSQL schema<br/>
· Documented crawl policy, data model, and SSM-based deployment workflows
</span>

<span style="font-size:12px;color:#57606a;display:block;margin-bottom:10px;">
<code>PostgreSQL</code> · <code>AWS RDS</code> · <code>SSM</code> · <code>Python</code> · <code>SQL migrations</code>
</span>

<pre style="font-size:11px;line-height:1.5;color:#57606a;background:#f6f8fa;border:1px solid #d0d7de;border-radius:8px;padding:12px;margin:0;white-space:pre-wrap;word-wrap:break-word;">
LCA + company data → priority score → career-site crawl → job postings
</pre>

<span style="font-size:13px;display:block;margin-top:12px;">
<a href="https://github.com/nicole732470/jobpush" style="color:#0969da;">GitHub</a>
</span>

</div>

<br/>

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/nicole732470/nicole732470/output/github-contribution-grid-snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/nicole732470/nicole732470/output/github-contribution-grid-snake.svg">
  <img src="https://raw.githubusercontent.com/nicole732470/nicole732470/output/github-contribution-grid-snake.svg" width="100%" alt="contribution snake" style="max-width:100%;height:auto;">
</picture>

</div>
