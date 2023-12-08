from api.pc.shemas import PCSchemaAdd


async def assembly_pc(template_pc: PCSchemaAdd) -> PCSchemaAdd:
    new_components = template_pc.components
    new_components["CPU"] = "inter core i5 5400"
    return PCSchemaAdd(
        price=template_pc.price,
        components=new_components
    )
