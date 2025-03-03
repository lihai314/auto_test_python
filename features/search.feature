Feature: 百度搜索
  作为用户
  我想要能够在百度上搜索信息
  以便找到相关的信息

  Background:
    Given 我在百度搜索页面

    Scenario Outline: 成功搜索
      When 我输入搜索词 "<search_term>"
      And 点击搜索按钮
      Then 我应该看到搜索结果
      Examples:
        | search_term |
        | python      |

    Scenario: 失败搜索
      When 我输入空的搜索词
      And 点击搜索按钮
      Then 我应该看到搜索结果
