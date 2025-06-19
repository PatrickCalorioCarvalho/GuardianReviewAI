import argparse
from langchain import PromptTemplate, LLMChain
from langchain_ollama.llms import OllamaLLM 

llm = OllamaLLM(model="qwen2.5-coder:1.5b")

prompt_template = """
Você é um especialista em revisão de código. Abaixo está uma alteração no código representada por um git diff:
{git_diff}

Por favor, forneça uma avaliação técnica dessa alteração. Identifique possíveis problemas ou melhorias e explique o raciocínio.
"""
prompt = PromptTemplate(
    input_variables=["git_diff"],
    template=prompt_template
)
chain = LLMChain(llm=llm, prompt=prompt)

def review(git_diff):
    return chain.run(git_diff=git_diff)

def main():
    parser = argparse.ArgumentParser(description="git diff")
    parser.add_argument("--git_diff_file", type=str, help="send path git diff")
    args = parser.parse_args()

    with open(args.git_diff_file, "r") as file:
        git_diff = file.read()

    result = review(git_diff)
    print(result)

if __name__ == "__main__":
    main()