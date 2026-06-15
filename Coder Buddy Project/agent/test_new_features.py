from agent.tools import get_template

def test_templates():
    print("Testing get_template tool...")
    
    # 1. Test existing template
    auth_fastapi = get_template.run("auth_fastapi")
    assert "FastAPI JWT User Authentication Template" in auth_fastapi
    print("[+] auth_fastapi retrieved successfully.")
    
    auth_frontend = get_template.run("auth_frontend")
    assert "Authentication Portal" in auth_frontend
    print("[+] auth_frontend retrieved successfully.")
    
    deploy_docker = get_template.run("deploy_docker")
    assert "Dockerfile" in deploy_docker
    print("[+] deploy_docker retrieved successfully.")

    # 2. Test non-existent template
    error_msg = get_template.run("invalid_template")
    assert "ERROR" in error_msg
    print("[+] Error response for invalid template verified.")
    
    print("\n[SUCCESS] All templates verified successfully!")

if __name__ == "__main__":
    test_templates()
