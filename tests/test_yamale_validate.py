from pytest import raises

from conftest import set_module_args, AnsibleExitJson, AnsibleFailJson


def test_import_module_works():
    import yamale_validate


def test_valid_yaml(module_args):
    import yamale_validate

    set_module_args({
        **module_args,
        "data_path": "tests/data_good.yaml"
    })

    with raises(AnsibleExitJson) as result:
        yamale_validate.main()

    assert (result.value.args[0]['changed'] is False)


def test_invalid_yaml(module_args):
    import yamale_validate

    set_module_args({
        **module_args,
        "data_path": "tests/data_bad.yaml"
    })

    with raises(AnsibleFailJson) as result:
        yamale_validate.main()

    assert (result.value.args[0]['changed'] is False)


def test_yaml_with_additional_fields_fails_in_strict_mode(module_args):
    import yamale_validate

    set_module_args({
        **module_args,
        "data_path": "tests/data_additional_field.yaml"
    })

    with raises(AnsibleFailJson) as result:
        yamale_validate.main()

    assert (result.value.args[0]['changed'] is False)


def test_yaml_with_additional_fields_fails_in_strict_mode(module_args):
    import yamale_validate

    set_module_args({
        **module_args,
        "data_path": "tests/data_additional_field.yaml",
        "strict": False
    })

    with raises(AnsibleExitJson) as result:
        yamale_validate.main()

    assert (result.value.args[0]['changed'] is False)
