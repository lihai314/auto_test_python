Feature: 登录
  作为已经注册成功的用户
  我想要登录系统后台
  以便进行后续操作

  Background:
    Given 我在登录页面

    Scenario Outline: 成功登录
      When 我输入用户名 "<username>" 和密码 "<password>"
      And 点击登录按钮
      Then 我应该看到登录成功后的页面
      Examples:
        | username | password |
        | 13226689104 | max888888 |

    Scenario Outline: 失败登录
      When 我输入用户名 "<username>" 和密码 "<password>"
      And 点击登录按钮
      Then 我应该看到密码错误的提示消息框
      Examples:
        | username | password |
        | 13226689104 | test_fault_password |
