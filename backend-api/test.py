import json_repair

json_string = """[
  {
    "id": 1,
    "title": "Header",
    "isCurrent": true,
    "content": {
      "current": {
        "title": 'Null',
        "subTitle": 'null',
        "cta": [
          "Contact",
          "Pricing"
        ],
        "otherContents": "<div><a href=\"https://www.producthunt.com/posts/budget-kanban\"><div>We're live on Product Hunt 🚀.<span>Check us out!</span></div></a><div>Budget Kanban</div><div><a href=\"mailto://support@budgetkanban.com\">Contact</a><a>Pricing</a></div></div>"
      },
      "suggestion": {
        "title": "The easiest way to manage your budgets",
        "subTitle": "Scale and track all your finances on one board.",
        "cta": [
          "Sign Up Now"
        ],
        "otherContents": 'null'
      }
    },
    "feedback": {
      "onCurrent": 'null',
      "onSuggestion": "The current header lacks a clear value proposition. It's better to have a benefit-driven statement that explains the core value proposition of the product to hook users. It is also important to have a clear primary CTA to encourage users to take action. The header also lacks visuals to reflect the brand identity and values",
    }
  },
  {
    "id": 2,
    "title": "Hero Section",
    "isCurrent": true,
    "content": {
      "current": {
        "title": "<h1>Prevent<span>budget mistakes</span>before they happen</h1>",
        "subTitle": "<p>Quickly identify budget overruns and misallocations from multiple projects using collaborative Kanban boards</p>",
        "cta": [
          "Start budgeting"
        ],
        "otherContents": "<div>Trusted by 25+ founders</div>"
      },
      "suggestion": {
        "title": "<h1>Focus on your project goals, not your budget.</h1>",
        "subTitle": "<p>Track multiple budgets across your team, prioritize expenses, and hit your targets with Budget Kanban.</p>",
        "cta": [
          "Try for Free"
        ],
        "otherContents": "<div>Trusted by thousands of project teams</div>"
      }
    },
    "feedback": {
      "onCurrent": "The current hero section lacks a clear explanation of the benefits of the product and fails to showcase the unique selling proposition. The CTA used is not benefit-driven and could be more specific.",
      "onSuggestion": "The suggestion provides a clear value proposition, an eye-catching hero image to build brand identity and more benefit-drive CTA text that will encourage users to sign up."
    }
  },
  {
    "id": 3,
    "title": "Benefits Section",
    "isCurrent": true,
    "content": {
      "current": {
        "title": "<div><h2>As your project grows, finances gets<span>messier</span></h2></div><div><span>Difficulty</span>in tracking real-time budget updates across multiple projects.</div><div><span>Stress</span>from trying to reconcile expenses at the end of each project.</div><div><span>Time wasted</span>on manual entry and adjustment of budget data.</div><div>Inability to quickly identify<span>budget overruns</span>or<span>misallocations.</span></div><div><span>Frustration</span>with the lack of a visually intuitive financial tracking system.</div><div><p>Only if there's a<span>visual financial tracking tool</span>that simplifies budget management for your projects 🤔So you can<span>oversee project finances at a glance</span>Importantly, so you can<span>make informed decisions promptly</span>😌</p><p>... like a Trello board, but for your budget! 💡</p></div><div><h2>Achieve that with<span>Budget Kanban</span></h2><div><span>Real-time visibility</span>into each project's financial status</div><div><span>Stress relief</span>from having an organized and easily understandable financial overview</div><div><span>Reduction of time</span>spent on manual data entry and corrections</div><div>Enhanced ability to<span>identify</span>and<span>rectify budget issues</span>swiftly</div><div><span>Increased accuracy</span>in budget allocation and monitoring</div></div>",
        "subTitle": 'null',
        "cta": 'null',
        "otherContents": 'null'
      },
      "suggestion": {
        "title": "<h2>Simplify your budget management, eliminate financial stress</h2><p>BudgetKanban is a visual financial management solution that drives efficiency and clarity in budget planning and tracking. With BudgetKanban, you will:</p><ul><li>Reduce manual errors and time wasted on manual data entry and corrections</li><li>Instantly access and track multiple budget reports for each project, </li><li>Be prompted of potential overruns and misallocations in real-time</li><li>Easily collaborate with your team for project budgeting </li></ul>",
        "subTitle": 'null',
        "cta": 'null',
        "otherContents": 'null'
      }
    },
    "feedback": {
      "onCurrent": "The current benefits section exists as a list of problems and does not have an easy-to-follow structure. It conveys the message but could use more visual support. The suggested improvement provides the key highlights at a glance and would be easier to read, follow and more memorable to the audience. There is no clear benefit-driven single CTA.",
      "onSuggestion": "The new benefits section provides a concise, benefit-driven message. It tells the users what they want and how your service will help. The formatting and structure of the suggested improvement make it easier to read and understand. The addition of images or infographics could enhance this section, and the addition of a single CTA can further increase conversion rates."
    }
  },
  {
    "id": 4,
    "title": "Pricing Section",
    "isCurrent": true,
    "content": {
      "current": {
        "title": "<div><div>Pricing</div><h1>Prevent Unexpected Expenses,Save Time and Money</h1></div><div><span>50% off</span><span>during March</span></div><div><h3>Single Project</h3><p>For individuals and small teams who manage a single project.</p></div><div>$5</div><div>$8</div><div>Per month. Billed monthly</div><div>Unlimited budget cards</div><div>Calculated formulas for insights</div><div>5 collaborators at a time</div><div>1 Kanban board</div><div><a href=\"/login\">Start budgeting</a><div>Cancel anytime</div></div><div><h3>Multiple Projects</h3><p>For individuals and businesses who manage multiple projects.</p></div><div>$9</div><div>$18</div><div>Per month. Billed monthly</div><div>Unlimited budget cards</div><div>Calculated formulas for insights</div><div>20 collaborators at a time</div><div>Unlimited Kanban boards</div><div><a href=\"/login\">Start budgeting</a><div>Cancel anytime</div></div><div>Popular</div><div><h3>Lifetime Deal</h3><p>For individuals and businesses who want to save money in the long run.</p></div><div>$89</div><div>$178</div><div>Pay once. No monthly or yearly fees</div><div>Unlimited budget cards</div><div>Calculated formulas for insights</div><div>20 collaborators at a time</div><div>Unlimited Kanban board</div><div>Pay once and use it forever</div><div><a href=\"/login\">Start budgeting</a><div>One time payment. No subscription</div></div>",
        "subTitle": 'null',
        "cta": 'null',
        "otherContents": 'null'
      },
      "suggestion": {
        "title": "<h2>Flexible budgeting for everyone</h2><p>BudgetKanban offers flexible pricing for budgeting needs of small to large businesses. Try the free plan for small teams. Upgrade based on your needs.</p><ul><li>Single project package for individuals and small teams</li><li>Unlimited Kanban boards for multiple projects</li><li>Lifetime deal for established businesses</li></ul>",
        "subTitle": "<div>Streamline your finances today</div>",
        "cta": [
          "Choose your plan"
        ],
        "otherContents": 'null'
      }
    },
    "feedback": {
      "onCurrent": "The current pricing section fails to give a clear breakdown of the pricing plans, lacking a clear benefit-driven message. It does not showcase an easy-to-read table with clear differentiation between plans, and the call-to-action is buried inside links. ",
      "onSuggestion": "The suggested improvement provides a clear message and benefits of using each pricing package. The call-to-action is now benefit-driven and more prominently displayed. A clear and more straightforward pricing table can help customers make a better decision. Providing an option for a free plan would also help increase conversions."
    }
  },
  {
    "id": 5,
    "title": "Testimonials Section",
    "isCurrent": true,
    "content": {
      "current": {
        "title": "<div><h1>Here's what founders and indiemakers are saying</h1><div><p>“This is really cool! Finance apps need a user interface (UI) overhaul and this is the solution.”</p><div><div>Arch, Founder of Schola</div><a href=\"https://twitter.com/archie_wyles\">@archie_wyles</a></div></div><div><div><div>Dan Mindru, Morning Maker Show</div><a href=\"https://twitter.com/d4m1n\">@d4m1n</a></div><p>“This is freaking awesome. It looks freaking fantastic. The design is so nice. It's so simple, it's so elegant.”</p></div><div><div><div>Sandra Djajic, Morning Maker Show</div><a href=\"https://twitter.com/TakoTreba\">@TakoTreba</a></div><p>“I LOVE THIS! ... People need to check this out... It looks so freakin’ good.”</p></div><div><div><div>Hieu, Founder of GasbyAI</div><a href=\"https://twitter.com/hieuSSR\">@HieuSSR</a></div><p>“Financial tracking in Kanban mode. Creative!”</p></div><div><div><div>Rossveth Lopez, Founder of FontVisual</div><a href=\"https://twitter.com/rossvethlopez\">@rossvethlopez</a></div><p>“Awesome UI and animation! It's also a fresh concept”</p></div><div><div><div>Victor Mak, Student</div><a href=\"https://twitter.com/victorevolves\">@victorevolves</a></div><p>“It is going to make personal budgetting so fun!”</p></div><div><div><div>Andrew, Founder of ClipPilot</div><a href=\"https://twitter.com/gratatouille23\">@gratatouille23</a></div><p>“The insights side window is a nice touch! Love how smooth the UI is.”</p></div><div><div><div>Mirza Leka, Fullstack Engineer</div><a href=\"https://twitter.com/mirzaleka\">@mirzaleka</a></div><p>“Wish my bank app had this feature”</p></div><div><div><div>Thaha, Founder of WriteFastAI</div><a href=\"https://twitter.com/TheHighSecond\">@TheHighSecond</a></div><p>“that is neatly done”</p></div></div>",
        "subTitle": 'null',
        "cta": 'null',
        "otherContents": 'null'
      },
      "suggestion": {
        "title": "<h2>Happy customers say it better</h2><p>See what our customers are saying about BudgetKanban</p><div><p>\"The best budgeting tool on the planet. Can't imagine starting a new project without BudgetKanban.\"</p><div><div>Brittany, Designer at Pixel</div></div></div><div><p>\"Financial tracking just got easier with BudgetKanban. The best workflow tool for the price.\"</p><div><div>John Doe, Founder of Doe Inc.</div></div></div>",
        "subTitle": 'null',
        "cta": 'null',
        "otherContents": 'null'
      }
    },
    "feedback": {
      "onCurrent": "The current testimonial section is too lengthy and hard-to-read. Including more specific testimonials would make it easier to resonate with the target audience and provide social proof and credibility. The style could be improved to reflect the brand's identity",
      "onSuggestion": "The suggestion provides a more concise and well-structured testimonial section that is easier to read and more relevant to the target audience. The suggested improvement features more specific testimonials and does not overwhelm users with several lines of feedback, adding credibility to the products. Including images and brief bios of the customers can also add social proof."
    }
  },
  {
    "id": 6,
    "title": "CTA Section",
    "isCurrent": true,
    "content": {
      "current": {
        "title": "<div><h2>Start budgeting with confidence today</h2><p>Take control of your budget and avoid unexpected expenses. Get started with Budget Kanban today.</p><div><button>Sign up for free</button><div><span>50% off</span><span>during March</span></div></div></div><div>Trusted by 25+ founders</div>",
        "subTitle": 'null',
        "cta": 'null',
        "otherContents": 'null'
      },
      "suggestion": {
        "title": "<div><h2>Take control of your budget and your projects</h2><p>Get started with Budget Kanban and avoid unexpected expenses, confusion and stress when managing your projects' finances. </p><div><button>Sign up for free</button><div><span>50% off</span><span>during March</span></div></div></div><div>Trusted by thousands of project teams</div>",
        "subTitle": 'null',
        "cta": 'null',
        "otherContents": 'null'
      }
    },
    "feedback": {
      "onCurrent": "The current CTA section doesn't provide sufficient information or compelling reasons for the user to take action. The focus is mostly on implementing the benefits of the product, but not on the actual conversion to customers. The forgot is buried in the text, and the form of CTA could be more benefit-driven.",
      "onSuggestion": "The suggested improvement provides a clear benefit-driven statement that will encourage the users to sign up. It provides a clear value proposition, urgency, and unrolling offer. The CTA button is more benefit-driven, located right after the value proposition, with clear and straightforward subtext. The suggestion also clearly states who this service is for, making it more personalized."
    }
  }
]"""


decoded_object = json_repair.loads(json_string)

print(decoded_object)