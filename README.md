# little flask project with simple CI pipeline
при пуше или пулл-реквесте в main в пайплайне устанавливаются все зависимости проекта и прогоняется один маленький тест
все это выполняется для версий python 3.8 и 3.9

пайплайн работает согласно файлу main.yml в .github/workflows. здесь реализована только CI

[![test_pipeline](https://github.com/nightblure/flask-site-ci-cd/actions/workflows/main.yml/badge.svg?branch=main&event=push)](https://github.com/nightblure/flask-site-ci-cd/actions/workflows/main.yml)
