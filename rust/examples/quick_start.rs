use crawlora_bbb::{BbbSearchParams, Client, ModelBbbSearchResponseDoc};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = std::env::var("CRAWLORA_API_KEY")?;
    let client = Client::new(api_key)?;
    let response = client
        .bbb
        .search(BbbSearchParams {
            query: Some("coffee".to_owned()),
            location: Some("New York, NY".to_owned()),
            ..Default::default()
        })
        .await?;
    let data: ModelBbbSearchResponseDoc = response.into_json()?;
    println!("{data:#?}");
    Ok(())
}
