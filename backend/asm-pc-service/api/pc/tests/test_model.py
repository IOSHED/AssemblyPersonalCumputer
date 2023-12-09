
from api.pc.model import TypeComponent, Component, PC
from api.pc.shemas import TypeComponentSchema, ComponentSchema, PCSchema


def test_type_component():
    type_component = TypeComponent(id=1, name="CPU")
    assert type_component.__repr__() == "TypeComponent(name='CPU')"
    assert type_component.to_read_model() == TypeComponentSchema(
        id=1,
        name="CPU",
    )


def test_component():
    component = Component(
        id=1,
        price=2000,
        user_rating_other_site=9.8,
        user_rating=2.4,
        type_component="CPU",
        name="Inter core i5 4655",
        specifications={"coolness": 100},
    )
    assert component.__repr__() == "Component(id=1, price=2000, name='Inter core i5 4655')"
    assert component.to_read_model() == ComponentSchema(
        id=1,
        price=2000,
        user_rating_other_site=9.8,
        user_rating=2.4,
        type_component="CPU",
        name="Inter core i5 4655",
        specifications={"coolness": 100},
    )


def test_pc():
    cpu = Component(
        id=1,
        price=2000,
        user_rating_other_site=9.8,
        user_rating=2.4,
        type_component="CPU",
        name="Inter core i5 4655",
        specifications={"coolness": 100},
    )
    gpu = Component(
        id=101,
        price=3000,
        user_rating_other_site=10,
        user_rating=10,
        type_component="GPU",
        name="NVIDIA GeForce 3020",
        specifications={"coolness": 101},
    )
    pc = PC(
        id=1,
        price=2000.3,
        components=[cpu, gpu],
    )
    assert pc.__repr__() == "PC(id=1, price=2000.3)"
    assert pc.to_read_model() == PCSchema(
        id=1,
        price=2000.3,
        components=[ComponentSchema(
            id=1,
            price=2000,
            user_rating_other_site=9.8,
            user_rating=2.4,
            type_component="CPU",
            name="Inter core i5 4655",
            specifications={"coolness": 100},
        ), ComponentSchema(
            id=101,
            price=3000,
            user_rating_other_site=10,
            user_rating=10,
            type_component="GPU",
            name="NVIDIA GeForce 3020",
            specifications={"coolness": 101},
        )]
    )
